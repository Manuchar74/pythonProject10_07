import pytest

@pytest.fixture
def fixture_filter_by_state():
    return ({'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'})

@pytest.fixture
def fixture__sort_by_date():
    return ({'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'})

@pytest.fixture
def fixture_get_mask_card_number():
        return "7158300734726758"