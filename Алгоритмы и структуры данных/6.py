from time import time
from random import randint


def main(some_list, number):
    counter = 0 # считает количество отрезков
    n = 0 # число на которое делятся отрезки
    while True: # пока не найдёт число, то будет повторятся

        if counter != int(number): # Если число не равно пользовательскому воду, то
            n += 1 # прибавляем единицу
            counter = 0 # обновляем количество отрезков
        else: # Иначе
            print(n) # Вывод числа
            break # Выход
        for i in some_list: # для каждого элемента в списке
            counter += int(i) // int(n) # прибавляем количество отрезком отдельного провода


#Опрост пользователся
def request_user():
    inp_1 = input().split(" ")
    n = inp_1[1]
    s_l = []
    for i in range(int(inp_1[0])):
        s_l.append(input())
    return [n, s_l]


def random_():
    N = randint(0, 1000)
    K = randint(0, 1000)
    l = []
    for i in range(N):
        l.append(randint(0, 1000))
    t = time()  # Для времени

    print("--", N)
    print("++", K)
    print(l)
    main(l, K)  # Запуск программы
    print("Ваше время = {}".format(time() - t))  # время


if __name__ == '__main__':
    # t = time() # Для времени
    # r_u = request_user() # Опрос порльзователя
    # main(r_u[1], r_u[0]) # Запуск программы
    # print("Ваше время = {}".format(time() - t)) # время
    random_() #для запуска рандомайзера
