import pytest

from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card


def test_get_mask_card_number():
    assert get_mask_card_number(card_number="7158300734726758") == "7158 30** **** 6758"
    assert get_mask_card_number(card_number="1596837868705199") == "1596 83** **** 5199"
    assert get_mask_card_number(card_number="6831982476737658") == "6831 98** **** 7658"
    assert get_mask_card_number(card_number="8990922113665229") == "8990 92** **** 5229"
    assert get_mask_card_number(card_number="5999414228426353") == "5999 41** **** 6353"
    with pytest.raises(Exception):
        assert not (len(card_number='59994142')) == 16


def test_get_mask_account():
    assert get_mask_account(user_account='73654108430135874305')
    assert get_mask_account(user_account='64686473678894779589')
    assert get_mask_account(user_account='35383033474447895560')
    with pytest.raises(Exception):
        assert not (len(user_account='353830334744')) == 20


@pytest.mark.parametrize("string, expected_result", [
    ('Счет 64686473678894779589', ('64686473678894779589', 'Счет ', False)),
    ('Visa Classic 6831982476737658', ('6831982476737658', 'Visa Classic ', True)),
    ])
def test_mask_account_card(string, expected_result):
    assert mask_account_card(string) == expected_result

