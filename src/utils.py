from datetime import datetime
import json
from src.operation import Operation


def open_json(path):
    '''
    Распаковка данных из файла JSON в список
    :param path: путь к файлу
    :return: список со словарями
    '''
    with open(path, 'r', encoding='utf-8') as file:
        return json.loads(file.read())


def class_packing(data):
    '''
    функция упаковывает список словарей в список с экземплярами
    :param data: список со словарями для упаковки в экземпляр класса
    :return: список с экземплярами класса Operation
    '''
    class_list = []
    for operation in data:
        if len(operation) == 7:
            class_list.append(Operation(
                operation["id"], operation["date"], operation["state"],
                operation["operationAmount"]["amount"],
                operation["operationAmount"]["currency"]["name"],
                operation["operationAmount"]["currency"]["code"],
                operation["description"], operation["to"], from_=operation["from"]))
        elif len(operation) == 6:
            class_list.append(Operation(
                operation["id"], operation["date"], operation["state"],
                operation["operationAmount"]["amount"],
                operation["operationAmount"]["currency"]["name"],
                operation["operationAmount"]["currency"]["code"],
                operation["description"], operation["to"]))
    return class_list


def operation_sort_from_executed(operation_list):
    '''
    функция сортирует экземпляры класса операций оставляя только выполненые
    :param operation_list: список экземпляров класса операции для сортировки
    :return: отсортированный список
    '''
    executed_operations = []
    for operation in operation_list:
        if operation.get_status():
            executed_operations.append(operation)
    return executed_operations


def operation_sort_from_date(operation_list):
    '''
    функция сортирует список экземпляров по дате в атрибуте
    :param operation_list: список для сортировки
    :return: отсортированный список последних 5
    '''
    sorted_list = sorted(operation_list)
    last_5 = sorted_list[-5:]
    last_5.reverse()
    return last_5


def date_formated(date):
    '''
    функция форматирует дату для пользователя
    :param date: дата в формате isoformat(sep='T')
    :return: отформатированную дату
    '''
    date_object = datetime.fromisoformat(date)
    formatted_date = date_object.strftime("%d.%m.%Y")
    return formatted_date


def account_disguise(account_number):
    '''
    маскирует номер карты или счета
    :param account_number: тип счета и его числовое значение
    :return: замаскированный номер счета
    '''
    if account_number:
        card_number = account_number.split(" ")
        if card_number[0] == "Счет":
            card_name = card_number[0]
            code_number = ''.join(list(card_number[-1])[-4:])
            return f"{card_name} **{code_number}"
        else:
            card_name = " ".join(card_number[:-1])
            code_number = f"{''.join(list(card_number[-1])[:4])} {''.join(list(card_number[-1])[4:6])}" \
                          f"** **** {''.join(list(card_number[-1])[-4:])}"
            return f"{card_name} {code_number}"
    else:
        return None
