#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Решите следующую задачу: напишите функцию, которая считывает
# с клавиатуры числа и перемножает их до тех пор, пока не будет введен 0.
# Функция должна возвращать полученное произведение. Вызовите функцию
# и выведите на экран результат ее работы.

def multiply_numbers():
    result = 1
    while True:
        number = int(input("Введите число:"))
        if number == 0:
            break
        result *= number
    return result


if __name__ == "__main__":
    result = multiply_numbers()
    print("Результат:", result)
