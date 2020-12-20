from time import time


def main(l, a, b):
    str1 = "" # строка которая будет сравниватся
    swh = False # Переключатель
    for i in range(len(l)): # для каждого в списке
        str1 += l[i] # будет добавлятся элемент из списка
        str2 = "" # обновлятся следующая строка
        for j in range(i + 1, len(l)): # для каждого из последующих элементов списка
            if str1 != str2: # если строки не равны
                if str2 <= str1: # если строка 2 меньшей длины
                    str2 += l[j] # то будет добавлятся последующий элемент
                else:
                    break # иначе выход из второго списка, для оптимизации
            else: # Иначе
                print("0.0({})".format(str1)) # Если строки равны
                swh = True # то переключаем переключатель
                break # выходим из списка
    if not swh: # если после цикла строки не равны
        print(a/b) # то выводим результат деления


# Удаляет первые нули и точку из результата, и переводит это в список
def prepare_str(a, b):
    s_a = str(a/b)
    s_a = list(s_a)
    c = 0
    for i in range(len(s_a)):
        if s_a[i] == "0" or s_a[i] == '.':
            c += 1
        else:
            break
    s_a.reverse()
    for i in range(c):
        s_a.pop()
    s_a.reverse()
    main(s_a, a, b)


if __name__ == '__main__':
    ab = input().split(" ")
    t1 = time()
    prepare_str(int(ab[0]), int(ab[1]))
    print("Ваше время {}".format(time() - t1))
