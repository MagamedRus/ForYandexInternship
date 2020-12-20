from time import time
from random import randint

def main(l, cc):
    # Всё в функции вычесляется в квадрате,
    # что бы не приходилось в лишний раз извлекать
    ln = pow(l, 2) # Максимальная длина
    r = [] # будущий список станций

    for i in range(len(cc)): # Для каждого пользователя
        r.append([i, 0]) # Создаётся своя станция(i - номер пользователя)
        hc = list(cc) # Создание отдельной переменной для cc
        hc.pop(i) # Удаляем с этого списка текущий элемент,
        # что бы не находить самих себя
        for j in range(len(hc)): # Для всех клиентов кроме нас
            s1 = pow(cc[i][0] - hc[j][0], 2)
            s2 = pow(cc[i][1] - hc[j][1], 2)
            s = s1 + s2 # Вычесляем расстояние до нас
            if s <= ln: # Если он находится в нужном радиусе
                r[i][1] += 1 # то добавляем его в наш таксопарк

    # Сортирует полученный список по второму элементу
    for i in range(len(r)):
        for j in range(i, len(r)):
            if r[i][1] < r[j][1]:
                r[i], r[j] = r[j], r[i]
            # По не понятной мне причине, элементы меняются местами даже если они равны
            # По этому, здесь они меняются обратно
            if r[i][0] > r[j][0] and r[i][1] == r[j][1]:
                r[i], r[j] = r[j], r[i]

    # вывод
    for i in r:
        print(i[0], i[1])


def tester():
    rng = randint(2, 6)
    users = randint(4, 10)
    user_list = []

    for i in range(users):
        user_list.append([randint(100000, 1000000) / 100000, randint(100000, 1000000) / 100000])
    print(users, rng)

    for i in user_list:
        print(i[0], i[1])
    print("----")
    return rng, user_list


# Опрос пользователя
def request_user():
    inp1 = input().split(" ")
    rq_l = []
    for i in range(int(inp1[0])):
        r_u = input().split(" ")
        rq_l.append([float(r_u[0]), float(r_u[1])])

    return float(inp1[1]), rq_l


if __name__ == '__main__':
    arg1, arg2 = tester() #request_user()
    t1 = time()
    main(arg1, arg2)
    print("Ваше время = {}".format(time() - t1))
