import pytest

from src.widget import get_data
from src.widget import mask_account_card


@pytest.mark.parametrize("string, expected_result", [
    ('Счет 64686473678894779589', ('64686473678894779589', 'Счет ', False)),
    ('Visa Classic 6831982476737658', ('6831982476737658', 'Visa Classic ', True)),
])
def test_mask_account_card(string, expected_result):
    assert mask_account_card(string) == expected_result


@pytest.mark.parametrize("string, expected_result", [('2018-07-11T02:26:18.671407', '11.07.2018')])
def test_get_data(string, expected_result):
    assert get_data() == expected_result
