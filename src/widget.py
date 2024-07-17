import re


def has_cyrillic(text):
    return bool(re.search("[а-яА-Я]", text))


def mask_account_card(user_input: str) -> tuple[str, str, bool]:
    """Функция общей маскировки карты и счета,
    принимает на вход только один аргумент — строку,
    которая состоит из требуемых частей. Это может быть строка типа
    Visa Platinum 7000 7922 8960 6361
    , или Maestro 7000 7922 8960 6361, или Счет 73654108430135874305
     Разделять строку на 2 аргумента (отдельно имя, отдельно номер) нельзя!"""
    word_and_number = list(user_input)
    new_word = ""
    new_number = ""
    flag = False

    for i in word_and_number:
        if i.isalpha() or i == " ":
            new_word += i
        else:
            new_number += i

    if has_cyrillic(new_word):
        result1 = new_number
        result2 = new_word
    else:
        flag = True
        result1 = new_number
        result2 = new_word
    return result1, result2, flag


def get_data():
    """Напишите функцию, которая принимает на вход строку вида
    2018-07-11T02:26:18.671407 и возвращает строку с датой в виде
    11.07.2018
    """
#    data_time = datetime.datetime.now()
    data_time = '2018-07-11T02:26:18.671407'
    str_data_time = str(data_time)
    split_data_time = str_data_time.split()
    date = split_data_time[0]
    day = date[8:10]
    month = date[5:7]
    year = date[0:4]

    return day + "." + month + "." + year
