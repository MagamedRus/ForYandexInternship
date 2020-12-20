from time import time

# объявление постоянных переменных
l_main = {}
c = 0
print("+ число(-а): добавить в стек\n-: удалить последнее из стека\n?: вывести наибольшее число\nstop: прекратить ввод")
while True: #Повторяется пока не выйдет из цикла

    # Объявление обновляющихся переменных
    inp_c = input()
    t = time()
    inp = inp_c.split(" ")# Образываем список из строки по разделителю "пробел"
    st = ""
    min_of_l = []

    #Если +, то добавляем в стек последующие числа
    if inp[0] == "+":
        inp.__delitem__(0)
        l_main[c] = inp
        c += 1

    #Ecли -, то выводим в виде строки последний элемент в стеке и удаляем его
    if inp[0] == "-":
        for i in l_main[c - 1]:
            st += i + " "
        print(st)
        l_main.pop(c - 1)
        c -= 1

    #Eсли ?, то сначала добавляем все элементы со словаря в список, после сортируем его, и выводим наименьшую
    if inp[0] == "?":
        for i in range(len(l_main)): # Здесь можно было немного оптимизировать, но осталось мало времени
            for j in range(len(l_main[i])):
                min_of_l.append(int(l_main[i][j]))

        for i in range(len(min_of_l)):
            for j in range(len(min_of_l) - i - 1):
                if min_of_l[j] > min_of_l[j + 1]:
                    min_of_l[j], min_of_l[j + 1] = min_of_l[j + 1], min_of_l[j]

        print("Минимальный элемент - {}".format(min_of_l[0]))
    #Для словаря
    #Если "stop", то выходим из цикла, и выводим оставшиеся элементы в стеке
    
    if inp[0] == "stop":
        if l_main != {}:
            print("Осталось в стеке - {}".format(l_main))
        break

    print("Ваше время = {}".format(time() - t)) #Время выполнения команды
