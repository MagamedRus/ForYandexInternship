from time import time # Импорт времени


def do_iter(l1, l2):  # Вспомогательная функция
    count = 0
    for n in range(len(l2)): # для каждого в списке 2
        if l1 == l2[n]: # проверяем на схожесть строки из списка 1
            count = 1 # для суммирования
            l2[n] = -1 # для исключения повторения одинаковых элементов
            break # выход из цикла
    return count


def main(l_1, l_2):

    switch = False # переключатель

    for i in range(len(l_2)): # для каждого из списка 2
        for j in range(len(l_1)): # выполняем поиск из списка 1
            c = 0 # обнуляем подсчёт
            l1j = list(l_1[j]) # для сохранения первичности списка 1
            for m in range(len(l_1[i])): # для каждой буквы элемента из списка 1
                c += do_iter(l_2[i][m], l1j) # выполняется поиск на схожесть
                if c == len(l_1[i]): # если строка схожа с одной из оригинальной, то
                    switch = True # переключаем переключатель
        if switch: # если переключатель равен True
            print("1") # то выводим единицу
            switch = False # и сбрасывем переключатель
        else: # иначе
            print("0") # выводим ноль


# Обычный опрос пользователя
def request_user():
    inp_1 = input().split(" ")
    l1 = []
    l2 = []
    for i in range(int(inp_1[0])):
        l1.append(input().split(" "))

    for i in range(int(inp_1[2])):
        l2.append(input().split(" "))
    return [l1, l2]


if __name__ == '__main__':
    s = request_user() # запуск опроса пользоваетеля
    t = time()
    main(s[0], s[1]) # Запуск программы
    print("Ваше время = {}".format(time() - t)) # Время
