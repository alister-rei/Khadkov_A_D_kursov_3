class Operation:
    def __init__(self, id_, date, state, amount, name, money_code, description, to, from_=None):
        ''' атрибуты класса '''
        self.id = id_
        self.date = date
        self.state = state
        self.amount = amount
        self.name = name
        self.money_code = money_code
        self.description = description
        self.from_ = from_
        self.to = to

    def __repr__(self):
        ''' данные для разработчика '''
        return f"{self.id} = id_ | {self.date} = date | {self.state} = state | " \
               f"{self.amount} = amount | {self.name} = name | {self.money_code} = code | " \
               f"{self.description} = description | {self.from_} = from_ | {self.to} = to"

    def __lt__(self, other):
        ''' для сортировки экземпляров класса '''
        return self.date < other.date

    def __str__(self):
        ''' строка для вывода пользователю '''
        return f"{self.id}=id_, {self.date}=date, {self.state}=state, " \
               f"{self.amount}=amount, {self.name}=name, {self.money_code}=code, " \
               f"{self.description}=description, {self.from_}=from_, {self.to}=to"

    def get_id(self):
        ''' возвращает атрибут id '''
        return self.id

    def get_date(self):
        ''' возвращает атрибут date '''
        return self.date

    def get_status(self):
        ''' возвращает bool атрибута status '''
        return self.state == 'EXECUTED'

    def get_amount(self):
        ''' возвращает атрибут amount '''
        return self.amount

    def get_money_name(self):
        ''' возвращает атрибут name '''
        return self.name

    def get_money_code(self):
        ''' возвращает атрибут code '''
        return self.money_code

    def get_description(self):
        ''' возвращает атрибут description '''
        return self.description

    def get_card_number_from(self):
        ''' возвращает атрибут from_ '''
        return self.from_

    def get_card_number_to(self):
        ''' возвращает атрибут to '''
        return self.to
