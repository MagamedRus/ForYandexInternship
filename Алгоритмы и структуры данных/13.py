from time import time
from random import randint


def main(str1, str2):
    result = "" # ответ
    for i in range(len(str1)):  # для каждого символа в первой строке
        for j in range(len(str2)):  # для каждого символа во второй строке
            c = 0 # Для цикла while
            c1 = 0 # Для подсчета лексикографической величены
            c2 = 0 # Для подсчета лексикографической величены
            find = "" # Обнуление временного ответа
            # Пока символ из первой строки равен строке из второй
            while (i + c) < len(str1) and (j + c) < len(str2) and str1[i + c] == str2[j + c]:
                find += str2[j + c] # Добавляем в временный ответ симвовы
                c += 1 # для подсчета следующего символа

            if len(find) > len(result): # Если длина времменого ответа больше чем окончательного
                result = find # то оканчательный ответ равняется временному
            elif len(find) == len(result): # Если же их длина равна
                # То подсчитывается лексикографическая разность
                for m in result:
                    for n in find:
                        if m > n:
                            c1 += 1
                        elif m < n:
                            c2 += 1
                # И присваивается меньшая из них
                if c2 < c1:
                    result = find
    print(result) # Вывод


# Опрос пользователя
def request_user():
    str1 = input()
    str2 = input()

    return [str1, str2]


# Тестер
def tester():
    letters = "aseyuasdf"
    s1 = ""
    s2 = ""
    for i in range(200):
        s1 += letters[randint(0, len(letters) - 1)]
    for i in range(200):
        s2 += letters[randint(0, len(letters) - 1)]
    print(s1 + "\n" + s2)
    main(s1, s2)


if __name__ == '__main__':
    #r_u = request_user()
    t1 = time()
    #main(r_u[0], r_u[1])
    tester()
    print("Время выполнения программы = {}".format(time() - t1))
