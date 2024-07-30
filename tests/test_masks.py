import pytest
from src.masks import get_mask_card_number, get_mask_account
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card, get_data



def test_get_mask_card_number(fixture_get_mask_card_number):
    assert get_mask_card_number(fixture_get_mask_card_number) == "7158 30** **** 6758"


def test_get_mask_account():
    assert get_mask_account(user_account='73654108430135874305')
    assert get_mask_account(user_account='64686473678894779589')
    assert get_mask_account(user_account='35383033474447895560')


    with pytest.raises(Exception):
        assert not (len(user_account='353830334744')) == 20










