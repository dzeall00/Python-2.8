#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Решить индивидуальное задание лабораторной работы 2.6,
# оформив каждую команду в виде отдельной функции.

import bisect
import re
import sys


def get_route():
    """
    Запросить данные о маршруте.
    """
    start = input("Введите начальный пункт: ")
    end = input("Введите конечный пункт: ")
    count = int(input("Введите номер маршрута: "))

    return {
        'начальный пункт': start,
        'конечный пункт': end,
        'номер маршрута': count
    }


def display_routes(routes):
    """
    Отобразить список маршрутов.
    """
    if routes:
        line = '+-{}-+-{}-+-{}-+'.format(
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^30} | {:^20} | {:^8} |'.format(
                "Начало",
                "Конец",
                "Номер"
            )
        )
        print(line)
        for route in routes:
            print(
                '| {:<30} | {:<20} | {:>8} |'.format(
                    route.get('начальный пункт', ''),
                    route.get('конечный пункт', ''),
                    route.get('номер маршрута', '')
                )
            )
        print(line)
    else:
        print("Список маршрутов пуст.")


def select_routes(routes, name_punct):
    """
    Выбрать маршруты с заданным пунктом отправления или прибытия.
    """
    selected = []
    for route in routes:
        if str(route['номер маршрута']) == name_punct:
            selected.append(route)
    return selected


def main():
    """
    Главная функция программы.
    """
    routes = []
    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            route = get_route()
            if route not in routes:
                bisect.insort(
                    routes, route, key=lambda item: item.get(
                        'номер маршрута'
                    )
                )
            else:
                print("Данный маршрут уже добавлен.")

        elif command == 'list':
            display_routes(routes)

        elif (m := re.match(r'select (.+)', command)):
            name_punct = m.group(1)
            selected = select_routes(routes, name_punct)
            display_routes(selected)

        elif command == 'help':
            print("Список команд:")
            print("add - добавить маршрут;")
            print("list - вывести список маршрутов;")
            print("select <номер маршрута> - запросить маршруты, которые имеют данный номер")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
