import pytest
from src.masks import get_mask_card_number, get_mask_account
from src.processing import filter_by_state, sort_by_date
from src.widget import mask_account_card, get_data
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


@pytest.mark.parametrize("string, expected_result", [
   ('2018-07-11T02:26:18.671407', '11.07.2018')])
def test_get_data(string, expected_result):
    assert get_data() == expected_result


def test_filter_by_state():
    assert filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]) == [
               {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
               {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_sort_by_date():
    assert sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]) == [
               {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
               {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

def test_mask_account_card(string, expected_result):
    assert mask_account_card(string) == expected_result


