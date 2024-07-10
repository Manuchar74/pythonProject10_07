def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску.
    Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX
    Т. е. видны первые 6 цифр и последние 4, номер разбит по блокам по 4 цифры,
    разделенным пробелами.
    """
    number = list(card_number)
    slice_object_1 = slice(0, 4, 1)
    slice_number_1 = number[slice_object_1]
    slice_object_11 = slice(4, 6, 1)
    slice_number_11 = number[slice_object_11]
    slice_object_2 = slice(12, 16, 1)
    slice_number_2 = number[slice_object_2]
    z = (
        "".join(slice_number_1)
        + " "
        + "".join(slice_number_11)
        + "** ****"
        + " "
        + "".join(slice_number_2)
    )

    return z


def get_mask_account(user_account: str) -> str:
    """
    Функция принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате
    **XXXX
    Т. е. видны только последние 4 цифры.
    Пример работы функции, возвращающей маску счета
    73654108430135874305  # входной аргумент
    **4305  # выход функции
    """
    number = list(user_account)
    slice_object_1 = slice(16, 20, 1)
    slice_number_1 = number[slice_object_1]
    z = "**" + "".join(slice_number_1)

    return z
