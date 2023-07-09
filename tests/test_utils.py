import src.utils
from src.operation import Operation

data_py = [{'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075',
            'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}},
            'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'},
           {'id': 142264268, 'state': 'CANCELED', 'date': '2019-04-04T23:20:05.206878',
            'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
            'to': 'Счет 75651667383060284188'}]

exemplar_list = [Operation(587085106, '2018-03-23T10:45:06.972075', 'EXECUTED',
                           '48223.05', 'руб.', 'RUB', 'Открытие вклада',
                           'Счет 41421565395219882431'),
                 Operation(142264268, '2019-04-04T23:20:05.206878', 'CANCELED',
                           '79114.93', 'USD', 'USD', 'Перевод со счета на счет',
                           'Счет 75651667383060284188',
                           from_='Счет 19708645243227258542')]




def test_open_json():
    assert src.utils.open_json("tests/tests_data.json") == data_py


def test_class_packing_1():
    test_class_packing = src.utils.class_packing(data_py)
    test_piece = test_class_packing[0]
    assert exemplar_list[0].get_id() == test_piece.get_id()
    assert exemplar_list[0].get_date() == test_piece.get_date()
    assert exemplar_list[0].get_amount() == test_piece.get_amount()
    assert exemplar_list[0].get_status() == test_piece.get_status()
    assert exemplar_list[0].get_description() == test_piece.get_description()
    assert exemplar_list[0].get_card_number_from() == test_piece.get_card_number_from()
    assert exemplar_list[0].get_card_number_to() == test_piece.get_card_number_to()
    assert exemplar_list[0].get_money_code() == test_piece.get_money_code()
    assert exemplar_list[0].get_money_name() == test_piece.get_money_name()


def test_class_packing_2():
    assert exemplar_list[1].get_id() == 142264268
    assert exemplar_list[1].get_date() == '2019-04-04T23:20:05.206878'
    assert exemplar_list[1].get_amount() == '79114.93'
    assert exemplar_list[1].get_status() is False
    assert exemplar_list[1].get_description() == 'Перевод со счета на счет'
    assert exemplar_list[1].get_card_number_from() == 'Счет 19708645243227258542'
    assert exemplar_list[1].get_card_number_to() == 'Счет 75651667383060284188'
    assert exemplar_list[1].get_money_code() == 'USD'
    assert exemplar_list[1].get_money_name() == 'USD'


def test_operation_class():
    operation1 = exemplar_list[0]
    operation2 = exemplar_list[1]
    operation3 = Operation(587089106, '2018-03-23T10:45:06.972075', 'EXECUTED',
                           '483.05', 'руб.', 'RUB', 'Открытие вклада',
                           'Счет 41421565395219882431')
    operation1_str = "587085106=id_, 2018-03-23T10:45:06.972075=date, EXECUTED=state, 48223.05=amount, руб.=name, " \
                     "RUB=code, Открытие вклада=description, None=from_, Счет 41421565395219882431=to"
    operation1_repr = "587085106 = id_ | 2018-03-23T10:45:06.972075 = date | EXECUTED = state | 48223.05 = amount | " \
                      "руб. = name | RUB = code | Открытие вклада = description | None = from_ | Счет " \
                      "41421565395219882431 = to"
    assert operation1.__str__() == operation1_str
    assert operation1.__repr__() == operation1_repr
    assert operation2 > operation1
    assert not operation1 < operation3


def test_operation_sort_from_executed():
    executed_operation = Operation(587085106, '2018-03-23T10:45:06.972075', 'EXECUTED',
                                   '48223.05', 'руб.', 'RUB', 'Открытие вклада',
                                   'Счет 41421565395219882431')
    assert len(src.utils.operation_sort_from_executed(exemplar_list)) == 1
    assert executed_operation.get_id() == (src.utils.operation_sort_from_executed(exemplar_list)[0]).get_id()


def test_operation_sort_from_date():
    data_sorted = [Operation(142264268, '2019-04-04T23:20:05.206878', 'CANCELED',
                             '79114.93', 'USD', 'USD', 'Перевод со счета на счет',
                             'Счет 75651667383060284188',
                             from_='Счет 19708645243227258542'),
                   Operation(587085106, '2018-03-23T10:45:06.972075', 'EXECUTED',
                             '48223.05', 'руб.', 'RUB', 'Открытие вклада',
                             'Счет 41421565395219882431')]
    assert src.utils.operation_sort_from_date(exemplar_list)[0].get_date() == data_sorted[0].get_date()
    assert src.utils.operation_sort_from_date(exemplar_list)[1].get_date() == data_sorted[1].get_date()


def test_date_formated():
    date = '2019-04-04T23:20:05.206878'
    assert src.utils.date_formated(date) == "04.04.2019"


def test_account_disguise():
    assert src.utils.account_disguise("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert src.utils.account_disguise("Счет 64686473678894779589") == "Счет **9589"
    assert src.utils.account_disguise("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert src.utils.account_disguise("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"
    assert src.utils.account_disguise("Visa Platinum 8990922113665229") == "Visa Platinum 8990 92** **** 5229"
    assert src.utils.account_disguise(None) is None
