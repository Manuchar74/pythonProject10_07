from typing import Union


def filter_by_state(
    input_list: list[dict[str, Union[int, str]]], state="EXECUTED"
) -> list[dict[str, Union[int, str]]]:
    """принимает список словарей и опционально значение для ключа state
    (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей,
    содержащий только те словари, у которых ключ state
    соответствует указанному значению."""
    new_list = []
    for item in input_list:
        if "state" in item:
            if item.get("state") == state:
                new_list.append(item)
            else:
                continue
        else:
            continue

    return new_list


def sort_by_date(
    list_to_sort: list[dict[str, Union[int, str]]], ascending: bool = True
) -> list[dict[str, Union[int, str]]]:
    """принимает список словарей и необязательный параметр, задающий порядок
    сортировки (по умолчанию — убывание). Функция должна возвращать новый список,
    отсортированный по дате (date)."""

    sorted_products = sorted(
        list_to_sort, key=lambda d: d.get("date", 0), reverse=bool(ascending)
    )

    return sorted_products
