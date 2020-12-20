from time import time as tm  # Импортируем в программу библеотеку времени, как tm
import random


def main_(l):
    count = l[0] * l[1] * l[2]
    # сортировка пузырьком для трех элементов?
    for i in range(len(l)):
        for j in range(len(l) - 1):
            for k in range(len(l) - 2):
                if i != j and i != k and j != k:
                    if count < l[i] * l[j] * l[k]:
                        count = l[i] * l[j] * l[k]
    return count # Возвращаем наибольшее умножение трёх элементов


# Обычный request user
def request_user():
    print("Введите первую строку: ")
    r_user = int(input())
    l_ = []
    print("Введите остальные строки: ")
    for i in range(r_user):
        l_.append(int(input()))
    return l_


# для продения тестов
def tester():
    random_list = []
    col = random.randrange(3, 1000)
    print("Чисел в массиве - {}".format(col))
    for i in range(col):
        random_list.append(random.randrange(-1000, 1000))
    return random_list


if __name__ == '__main__':
    rq_user = tester()  # Присваиваем переменной значение request user
    t = tm()  # Время до программы
    m = main_(rq_user)  # Передаём значение выполнения request user, в функции main_
    print("Результат выполнения программы = {}".format(m))  # Выводим результат выполнения программы
    tester()
    print("Ваше время = {}".format(tm() - t))  # Вычесляем время выполнение программы, и выводим

