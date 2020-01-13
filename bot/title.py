import datetime

group_title = 'ИУ8-31'
numerator = 'чс'
denominator = 'зн'


def get_true_group_title():
    week = datetime.date.today().isocalendar()[1] - 35

    if week % 2 == 0:
        sufix = denominator
    else:
        sufix = numerator

    return group_title + ' [' + str(week) + ' ' + sufix + ']'
