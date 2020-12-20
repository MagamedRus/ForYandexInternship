from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text
import sqlalchemy as sa
import xlrd
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


if __name__ == "__main__":
    DB_PATH = "sqlite:///data_base.sqlite3"
    from class_db import *

elif __name__ == "data_base.work_db":
    DB_PATH = "sqlite:///data_base/data_base.sqlite3"
    from data_base.class_db import * # Подключение модулей и библеотек


Base = declarative_base()


def engine_session():
    engine = sa.create_engine(DB_PATH)
    sessions = sessionmaker(engine)
    session = sessions()
    return session


def add_exchange_data(l1, l2, l3, l4, l5):
    session = engine_session()
    new_course = Exchange_Date(
        code=l1,
        codeA=l2,
        units=l3,
        name=l4,
        course=l5
        )
    session.add(new_course)
    session.commit()


#Добавление пасспорта
def add_user_passport(l1, l2, l3, l4, l5, l6, l7, l8, l9, l10):
    session = engine_session()
    User_Pass = User_Passport(
        firstName=l1,
        secondName=l2,
        lastName=l3,
        sex=l4,
        birthday=l5,
        dateOfGet=l6,
        codeOfReg=l7,
        birthPlace=l8,
        serial=l9,
        number=l10
        )
    session.add(User_Pass)
    session.commit()


def add_user_action(l1, l2, l3, l4, l5, l6,
                    l7, l8, l9):
    session = engine_session()
    add_user = User_Data_Action(
        date=l1,
        codeM1=l2,
        codeM2=l3,
        sizeSend=l4,
        sizeGet=l5,
        secondName=l6,
        course=l7,
        codeB=l8,
        selfCode=l9
        )
    session.add(add_user)
    session.commit()


def add_banks(l1, l2):
    session = engine_session()
    bank = Banks_Data(
        code=l1,
        name=l2,

    )
    session.add(bank)
    session.commit()


#Создание списка для валют
def read_xls_for_exchange():
    rd = xlrd.open_workbook('spisok.xls', formatting_info=True)
    sheet = rd.sheet_by_index(0)

    l = sheet.nrows
    for i in range(l - 2):
        if sheet.row_values(i + 2)[2] not in s_lis:
            print(sheet.row_values(i + 2)[2])
            s = input()
            add_each_city_data(s, sheet.row_values(i + 2)[2])
            s_lis.append(sheet.row_values(i + 2)[2])
        else:
            print("+")


def find_and_remake_db():
    session = engine_session()
    query = session.query(Each_City)
    q_all = query.all()
    s_lis = []
    rd = xlrd.open_workbook('spisok.xls', formatting_info=True)
    sheet = rd.sheet_by_index(0)
    l = sheet.nrows
    counter = 0
    c = 0
    for j in range(l - 2):
        if sheet.row_values(j + 2)[2] in s_lis:
            counter += 1
            code = str(q_all[c].code) + str(counter)
            add_each_city_data(sheet.row_values(j + 2)[1], code)
        else:
            counter = 1
            s_lis.append(sheet.row_values(j + 2)[2])
            code = str(q_all[c].code) + str(counter)
            add_each_city_data(sheet.row_values(j + 2)[1], code)
            c += 1


def add_exchange_rate_from_xls():
    rd = xlrd.open_workbook('valut.xls', formatting_info=True)
    sheet = rd.sheet_by_index(0)
    l = sheet.nrows
    for j in range(l - 1):
        add_exchange_data(sheet.row_values(j+1)[0],
                          sheet.row_values(j+1)[1],
                          sheet.row_values(j+1)[2],
                          sheet.row_values(j+1)[3],
                          sheet.row_values(j+1)[4])


def add_bank_from_xls():
    rd = xlrd.open_workbook('valut.xls', formatting_info=True)
    sheet = rd.sheet_by_index(0)
    l = sheet.nrows
    for j in range(l - 1):
        add_banks(sheet.row_values(j+1)[1],
                  sheet.row_values(j+1)[0])


def make_selection():
    session = engine_session()
    query = session.query(Banks_Data)
    q_all = query.all()

    with open("some.txt", "w") as wr:
        for i in q_all:
            wr.write("<option>" + i.name + "</option>" + "\n")


def find_query(n_table, f_by):
    session = engine_session()
    q = session.query(n_table).filter_by(name=str(f_by)).first()
    return q


