def add_everything_up(a, b):        # add_everything_up(a, b) принимает a и b
    try:
        return round(a + b, 3)      # Если a и b одного типа, возвращаем их сумму с округлением до 3го знака после запятой
    except TypeError:
        return str(a) + str(b)      # Если a и b разного типа, возвращаем их строковое представление

# Примеры использования функции
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
# print(add_everything_up('яблоко', 'строка'))
