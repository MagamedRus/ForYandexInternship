from time import time
from random import randint


def main(l):
    c = 0 # Счётчик
    for i in range(len(l)): # Для каждого из списка
        if not l[i] == []:
            swh = False
            help_dict = {} # Обновляется словарь
            for j in l[i][0]: # Добавляются ключи в словарь
                help_dict[j] = 0

            for j in range(len(l[i][0])): # Подсчитываются количество этих ключей в словаре
                for m in help_dict:
                    if m == l[i][0][j]:
                        help_dict[m] += 1
            for m in range(i + 1, len(l)): # Для всех последующих элементво списка
                if not l[m][0] == []: # Для оптимизации кода
                    another_dict = {}  # Обновляется словарь
                    for j in l[m][0]: # Добавляются ключи в словарь
                        another_dict[j] = 0
                    for j in range(len(l[m][0])): # Подсчитываются количество этих ключей в словаре
                        for n in another_dict:
                            if n == l[m][0][j]:
                                another_dict[n] += 1

                    if help_dict == another_dict: # Если словари идентичны
                        swh = True # Переключается переключатель
                        l[m] = [[]] # очищается этот элемент в списке(что бы избежать повторения)
            if swh: # Если переключено
                c += 1 # то добавляем элемент в список

    print(c) # выводими результат


# Опрос пользователя
def request_user():
    l = []
    for i in range(int(input())):
        l.append([input()])
    return l


def tester():
    s = "ABCDEFGHJV"
    r = randint(5, 200)
    l = []
    for i in range(r):
        ss = ""
        for j in range(10):
            ss += s[randint(0, 3)]
        l.append([ss])
    print(r, "Количество строк")
    return l


if __name__ == '__main__':
    #r_u = request_user()
    t1 = time()
    r_u = tester()
    main(r_u)
    print("Ваше время = {}".format(time() - t1))
