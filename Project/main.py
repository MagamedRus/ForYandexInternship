import eel
import time
from plugins.another_plugins import *
from data_base.work_db import *


# numb, name_1, name_2, self_code, name_bank
@eel.expose
def convert_to(l):
    session = engine_session()
    q_1 = find_query(Exchange_Date, l[1])
    q_2 = find_query(Exchange_Date, l[2])
    course_1 = q_1.course
    course_2 = q_2.course
    codeM1 = q_1.code
    codeM2 = q_2.code
    codeB = session.query(Banks_Data).filter_by(name=l[4]).first().code
    date = str(time.strftime("%d-%m-%Y"))
    second_name = session.query(User_Passport).filter_by(number=l[3]).first().secondName

    if l[1] == "Российский рубль":
        result = course_1 * int(q_1.units) * int(l[0]) # Продано рублей
        add_user_action(
            date, # Дата
            codeM1, # Код первой валюты
            codeM2, # Код второй валюты
            l[0], # Проданная валюта
            round(result, 2), # Количество купленной валюты
            second_name, # Фамилия пользователя
            q_1.course, # Курс валюты
            codeB, # Код банка
            l[3] # Номер паспорта пользователя
        )
    elif l[2] == "Российский рубль":
        result = course_1 * int(q_1.units) * int(l[0])  # Продано рублей
        coeff = course_1 * int(q_1.units)
        add_user_action(
            date,
            codeM1,
            codeM2,
            round(result, 2),
            l[0],
            second_name,
            coeff,
            codeB,
            l[3]
        )
    else:
        coeff_1 = course_1 / int(q_1.units) * int(l[0])
        coeff_2 = course_2 / int(q_2.units)
        course = coeff_1 / coeff_2
        result = coeff_1 / coeff_2
        add_user_action(
            date,
            codeM1,
            codeM2,
            round(result, 2),
            l[0],
            second_name,
            course,
            codeB,
            l[3]
        )
    return round(result, 2)


@eel.expose
def add_passport_data(passport_list):
    add_user_passport(
        passport_list[0],
        passport_list[1],
        passport_list[2],
        passport_list[3],
        passport_list[4],
        passport_list[5],
        passport_list[6],
        passport_list[7],
        passport_list[8],
        passport_list[9],
    )


def make_report_str(dict_of_act):
    t_str = "\t\t\t\t"
    f_str = '{}<tr class="head">\n' \
            '{}\t<th>Банк</th>\n' \
            '{}\t<th>Дата</th>\n' \
            '{}\t<th>Клиент</th>\n' \
            '{}\t<th>Проданная валюта</tn>\n' \
            '{}\t<th>Купленная валюта</th>\n' \
            '{}\t<th>Куплено</th>\n' \
            '{}\t<th>Затрачено</th>\n' \
            '{}</tr>'.format(t_str, t_str, t_str, t_str,
                             t_str, t_str, t_str, t_str, t_str)

    for i in dict_of_act:
        c = len(dict_of_act[i])
        swt = False
        for j in range(c):
            if not swt:
                f_str += '\n{}<tr class="body">\n' \
                    '{}\t<td rowspan="{}" class="first-column">{}</td>\n' \
                    '{}\t<td>{}</td>\n' \
                    '{}\t<td>{}</td>\n' \
                    '{}\t<td>{}</td>\n' \
                    '{}\t<td>{}</td>\n' \
                    '{}\t<td>{}</td>\n' \
                    '{}\t<td>{}</td>\n' \
                    '{}</tr>\n'.format(t_str,
                                       t_str, c, i,
                                       t_str, dict_of_act[i][j][0],
                                       t_str, dict_of_act[i][j][1],
                                       t_str, dict_of_act[i][j][2],
                                       t_str, dict_of_act[i][j][3],
                                       t_str, dict_of_act[i][j][4],
                                       t_str, dict_of_act[i][j][5],
                                       t_str)
                swt = True
            else:
                f_str += '\n{}<tr class="body">\n' \
                         '{}\t<td>{}</td>\n' \
                         '{}\t<td>{}</td>\n' \
                         '{}\t<td>{}</td>\n' \
                         '{}\t<td>{}</td>\n' \
                         '{}\t<td>{}</td>\n' \
                         '{}\t<td>{}</td>\n' \
                         '{}</tr>\n'.format(t_str,
                                            t_str, dict_of_act[i][j][0],
                                            t_str, dict_of_act[i][j][1],
                                            t_str, dict_of_act[i][j][2],
                                            t_str, dict_of_act[i][j][3],
                                            t_str, dict_of_act[i][j][4],
                                            t_str, dict_of_act[i][j][5],
                                            t_str)

    return f_str


@eel.expose
def find_passport(code):
    session = engine_session()
    q = session.query(User_Passport).filter_by(number=code).first()
    return q.number


@eel.expose
def get_numb():
    session = engine_session()
    q = session.query(User_Passport).all()
    some_l = []
    for i in range(len(q)):
        some_l.append(q[i].number)
    return some_l


@eel.expose
def make_report():
    session = engine_session()
    q_act = session.query(User_Data_Action).all()
    dict_of_bank = {}

    for i in range(len(q_act)):
        codeB = q_act[i].codeB
        q_bank = session.query(Banks_Data).filter_by(code=codeB).first().name
        if q_bank not in dict_of_bank:
            dict_of_bank[q_bank] = []
            name_M1 = session.query(Exchange_Date).filter_by(code=q_act[i].codeM1).first().name
            name_M2 = session.query(Exchange_Date).filter_by(code=q_act[i].codeM2).first().name
            dict_of_bank[q_bank].append([q_act[i].date, q_act[i].secondName,
                                         name_M1, name_M2, q_act[i].sizeSend,
                                         q_act[i].sizeGet])
        else:
            name_M1 = session.query(Exchange_Date).filter_by(code=q_act[i].codeM1).first().name
            name_M2 = session.query(Exchange_Date).filter_by(code=q_act[i].codeM2).first().name
            dict_of_bank[q_bank].append([q_act[i].date, q_act[i].secondName,
                                        name_M1, name_M2, q_act[i].sizeSend,
                                        q_act[i].sizeGet])
    f_result = make_report_str(dict_of_bank)
    return f_result


if __name__ == '__main__':
    eel.init("web")
    eel.start("index.html", size=(1280, 1280))

