from src.masks import get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number(card_number="7158300734726758") == "7158 30** **** 6758"
