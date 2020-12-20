from time import time
from math import sqrt


# Находит ближайшее метро
def find_near_metro(los, p):
    s1 = p[0] - los[0][0]
    s2 = p[1] - los[0][1]
    r = pow(s1, 2) + pow(s2, 2)
    find_pos = list(p)

    for i in range(len(los)):
        s1 = p[0] - los[i][0]
        s2 = p[1] - los[i][1]
        s = pow(s1, 2) + pow(s2, 2)
        if s < r:
            r = s
            find_pos = los[i]

    return find_pos


def main(p1, p2, v1, v2, los, low):
    self_pos = find_near_metro(los, p1) # Ближайшее метро для своего местоположения
    exit_pos = find_near_metro(los, p2) # Ближайшее метро для конечного местоположения
    # Список наших местоположений
    result_list = [list(self_pos)] # Обёрнут в list для инициализации новой переменной, а не указателя
    result_str = str(los.index(self_pos) + 1) + " " # Единичка прибавляется для преобразования обратно в нумерацию, из индексирования
    self_ind = los.index(self_pos) # Находим свой индекс в списке мест метро, и отталкиваемся от него
    t = 0 # Для подсчета времени
    while exit_pos not in result_list: # Пока не попадём в нужное нам метро
        for i in range(len(low)): # Для каждого в списке путей
            if self_ind in low[i]: # Находим свой индекс
                for j in range(len(low[i])): # Для каждого индекса, в списке местоположений
                    if low[i][j] != self_ind: # Если индекс не равен нашему индексу
                        if low[i][j] != -1: # И результат не равен -1(Для того что бы наше местополежиние не равнялось -1)
                            self_ind = low[i][j] # Своё местоположение равняется соседнему индексу в списке
                            result_list.append(los[self_ind]) # Добавляем в список наши координаты(для цикла while)
                            result_str += str(self_ind + 1) + " " # И добавляем свой индекс в строку, для вывода ответа
                        low[i] = [-1, -1]  # Приравняем путь на -1, -1 для исключения повторения из одного метро в другое

    #Вычесление затраченного времеги на путь с метро и до метро
    s1 = p1[0] - self_pos[0]
    s2 = p1[1] - self_pos[1]
    t += sqrt(pow(s1, 2) + pow(s2, 2)) / v1 # Время до метро
    s1 = p2[0] - exit_pos[0]
    s2 = p2[1] - exit_pos[1]
    t += sqrt(pow(s1, 2) + pow(s2, 2)) / v1 # Время с метро
    last_dot = result_list[0] # Наше местоположение

    #Считает путь
    for i in range(1, len(result_list)):
        s1 = last_dot[0] - result_list[i][0]
        s2 = last_dot[1] - result_list[i][1]
        t += sqrt(pow(s1, 2) + pow(s2, 2)) / v2 # вычесляем время
        last_dot = result_list[i]  # обновляем наше местополоежние

    # Расчет времении пешком
    s1 = p1[0] - p2[0]
    s2 = p1[1] - p2[0]
    s = sqrt(pow(s1, 2) + pow(s2, 2)) / v1

    #Если пешком быстрее
    if s > t:
        print("Пешком быстрее!")
        print(round(s, 7)) # то выводим время пешего пути
    else: # Иначе
        print(round(t, 7)) # выводим затраченное время с метро
        print(result_str) # и станции с метро


#Каждый элемент списка преобразуется в int
def make_int(l):
    for i in range(len(l)):
        l[i] = int(l[i])
    return l


#Опрос пользователя
def request_user():
    some_l = [make_int(input().split(" "))] # Первая строка
    c = int(input()) # Вторая строка
    help_list = []
    for i in range(c): # Для следующих "c" строк
        help_list.append(make_int(input().split(" ")))
    some_l.append(help_list)
    help_list = []
    while True: # Для последующих строк, до "0 0"
        s = input()
        if s != "0 0":
            ss = make_int(s.split(" "))
            help_list.append([ss[0] - 1, ss[1] - 1])
        else:
            break
    some_l.append(help_list)
    some_l.append(make_int(input().split(" "))) # Предпоследняя строка
    some_l.append(make_int(input().split(" "))) # Последняя строка
    return some_l


if __name__ == '__main__':

    r_u = request_user()

    #Присваивание значений
    list_of_st = r_u[1]
    list_of_way = r_u[2]
    pun1 = r_u[3]
    pun2 = r_u[4]

    sped_of_man = r_u[0][0]
    speed_of_train = r_u[0][1]

    t1 = time() # Расчёт времени
    main(pun1, pun2, sped_of_man, speed_of_train, list_of_st, list_of_way)
    print("Ваше время = {}".format(time() - t1))
