import datetime


class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items


def add_item_to_cheque(self, name):
    if not 1 < len(name) < 41:
        raise ValueError(f"Нельзя добавить товар, если в его названии нет символов или их больше 40")
    elif name not in self.__item_price:
        raise NameError(f"Позиция отсутствует в товарном справочнике")
    else:
        self.__name_items.append(name)
        self.__number_items += 1


def delete_item_from_cheque(self, name):
    if name not in self.__item_price:
        raise NameError(f"Позиция отсутствует в чеке")
    else:
        self.__name_items.remove(name)
        self.__number_items -= 1


def check_amount(self):
    total = []
    for item in self.__name_items:
        total.append(self.__item_price[item])
    total_sum = sum(total)
    if self.__number_items > 10:
        total_sum *= 0.9
    return total_sum


def twenty_percent_tax_calculation(self):
    twenty_percent_tax = []
    total_tax = 0
    for item in self.__name_items:
        if self.__tax_rate[item] == 20:
            twenty_percent_tax.append(item)
            total_tax += self.__item_price[item] * 0.2
    return total_tax


def ten_percent_tax_calculation(self):
    ten_percent_tax = []
    total_tax = 0
    for item in self.__name_items:
        if self.__tax_rate[item] == 10:
            ten_percent_tax.append(item)
            total_tax += self.__item_price[item] * 0.1
    return total_tax


def total_tax(self):
    ten_percent_tax = self.ten_percent_tax_calculation()
    twenty_percent_tax = self.twenty_percent_tax_calculation()
    return ten_percent_tax + twenty_percent_tax


@staticmethod
def get_telephone_number(telephone_number):
    if not telephone_number.isdigit():
        raise ValueError('Необходимо ввести цифры')
    elif len(telephone_number) >= 11:
        raise ValueError('Необходимо ввести 10 цифр после "+7"')
    else:
        return print(f'+7{telephone_number}')


@staticmethod
def get_date_and_time():
    date_and_time = []
    now = datetime.datetime.now()
    date = [['часы', lambda x: x.hour], ['минуты', lambda x: x.minute], ['день', lambda x: x.day], ['месяц', lambda x: x.month], ['год', lambda x: x.year]]
    for item in date:
        date_and_time.append(f'{item[0]}: {item[1](now)}')
    return date_and_time
