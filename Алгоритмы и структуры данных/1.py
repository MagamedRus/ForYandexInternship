from time import time


def main(a, b, g):
    f_l = []
    a_l = a.split(" ")
    b_l = b.split(" ")

    #переумножение списков
    for i in range(g):
        for j in range(g):
            f_l.append(int(a_l[i])*int(b_l[j]))

    #Сортировка пузырьком
    for i in range(len(f_l)-1):
        for j in range(len(f_l)-i-1):
            if f_l[j] > f_l[j+1]:
                f_l[j], f_l[j+1] = f_l[j+1], f_l[j]

    count = len(f_l) // 10
    c = 0

    #Умножаем каждый десятый элемент
    for i in range(count + 1):
        i *= 10
        print(i, "+")
        print(f_l[i])
        c += f_l[i]

    print("Ответ", c)


if __name__ == '__main__':
    print("Ведите первую переменную")
    g = int(input())
    print("Ведите первый список")
    a = input()
    print("Ведите второй список")
    b = input()
    s = time()
    main(a, b, g)
    ss = time()
    print("Ваше время: ", ss - s)
