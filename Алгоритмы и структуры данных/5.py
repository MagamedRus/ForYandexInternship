from time import time as tm  # Импортируем в программу библеотеку времени, как tm


# Основная программа
def main_(req_user):
    req_user = req_user.split(" ")
    stack = []
    # Для каждого из списка, проверяем на символы
    for i in req_user:
        # Eсли элемент списка не операнд
        if i not in "+*-":
            stack.append(i)  # То кладём его в стек
        # Если это операнд, то производим вычесления с последними элементами из списка(попутно извлекая их из списка)
        elif i == "+":
            stack.append(int(stack.pop()) + int(stack.pop()))
        elif i == "*":
            stack.append(int(stack.pop()) * int(stack.pop()))
        elif i == "-":
            stack.append(int(stack.pop()) - int(stack.pop()))
    return stack


#Обычный request user
def request_user():
    print("Введите выражение: ")
    r_user = input()
    return r_user


# Запуск программы
if __name__ == '__main__':
    rq_user = request_user()  # Присваиваем переменной значение request user
    t = tm()  # Время до программы
    m = main_(rq_user)  # Передаём значение выполнения request user, в функции main_
    print("Результат выполнения программы = {}".format(m[0]))  # Выводим результат выполнения программы
    print("Ваше время = {}".format(tm() - t))  # Вычесляем время выполнение программы, и выводим
