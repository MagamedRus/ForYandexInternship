import sys


def request_user():

    print("Введите первую валюту")
    name_1 = input()

    print("Введите количество")
    numb = int(input())

    print("Введите вторую валюту")
    name_2 = input()

    calculate(numb, name_1, name_2)


def to_float(numb):
    print(type(numb))
    n1 = ""
    n2 = []
    for i in range(len(numb)):
        n2.append(numb[i])

    for i in range(len(n2)):
        if n2[i] == ",":
            n2[i] = "."

    for i in range(len(numb)):
        n1 += n2[i]

    return float(n1)


def make_list():
    some_str = ""
    session = engine_session()
    query = session.query(Exchange_Rates)
    q_all = query.all()
    for i in range(len(q_all)):
        some_str += "<li>" + q_all[i].name + "</li>" + "\n"

    with open("../data_base/some.txt", "w") as s:
        s.write(some_str)

