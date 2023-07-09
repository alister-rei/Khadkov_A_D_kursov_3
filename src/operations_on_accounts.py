from src import utils

JSON_FILE = "../operations.json"


def main():
    ''' открываем файл json '''
    json_list = utils.open_json(JSON_FILE)
    ''' упаковываем список словарей в список экземпляров класса Operation '''
    exemplar_list = utils.class_packing(json_list)
    ''' сортируем операции оставляя только выполненые '''
    executed_list = utils.operation_sort_from_executed(exemplar_list)
    ''' сортируем список классов по дате через свойство класса '''
    last_5_for_date = utils.operation_sort_from_date(executed_list)
    ''' получаем а после выводим информацию из каждого класса последовательно '''
    for exemplar in last_5_for_date:
        ''' получаем дату для пользователя через функцию '''
        date = utils.date_formated(exemplar.get_date())
        ''' получаем комментарий из экземпляра '''
        description = exemplar.get_description()
        ''' получаем откуда совершается перевод ,счет маскируется функцией '''
        whence = utils.account_disguise(exemplar.get_card_number_from())
        ''' получаем куда совершается перевод ,счет маскируется функцией '''
        where = utils.account_disguise(exemplar.get_card_number_to())
        ''' получаем сумма '''
        amount = exemplar.get_amount()
        ''' получаем наименование платежной единицы '''
        name = exemplar.get_money_name()
        ''' выводим данные для пользователя проверяя есть ли место отправления в случае открытия счета '''
        if whence:
            print(f"{date} {description}\n{whence} -> {where}\n{amount} {name}\n")
        else:
            print(f"{date} {description}\n{where}\n{amount} {name}\n")


if __name__ == "__main__":
    main()
