from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


#Валюта(не рабочая)
class Exchange_Rate(Base):
    __tablename__ = "Exchange_Rate"
    id = sa.Column(sa.Integer, primary_key=True)
    code = sa.Column(sa.Integer)
    codeA = sa.Column(sa.Text)
    units = sa.Column(sa.Integer)
    name = sa.Column(sa.Text)
    course = sa.Column(sa.Integer)


class Exchange_Date(Base):
    __tablename__ = "Exchange_Date"
    id = sa.Column(sa.Integer, primary_key=True)
    code = sa.Column(sa.Integer)
    codeA = sa.Column(sa.Text)
    units = sa.Column(sa.Integer)
    name = sa.Column(sa.Text)
    course = sa.Column(sa.Integer)


#Паспортные данные
class User_Passport(Base):
    __tablename__ = "User_Passport"
    id = sa.Column(sa.Integer, primary_key=True)
    firstName = sa.Column(sa.Text)
    secondName = sa.Column(sa.Text)
    lastName = sa.Column(sa.Text)
    sex = sa.Column(sa.Text)
    birthday = sa.Column(sa.Text)
    dateOfGet = sa.Column(sa.Text)
    codeOfReg = sa.Column(sa.Integer)
    birthPlace = sa.Column(sa.Text)
    serial = sa.Column(sa.Integer)
    number = sa.Column(sa.Integer)


#Области
class Each_City(Base):
    __tablename__ = "Each_City"
    id = sa.Column(sa.Integer, primary_key=True)
    code = sa.Column(sa.Integer)
    name = sa.Column(sa.Text)


#Города
class City(Base):
    __tablename__ = "City"
    id = sa.Column(sa.Integer, primary_key=True)
    code = sa.Column(sa.Integer)
    name = sa.Column(sa.Text)


#Использованные банки
class Banks_Used(Base):
    __tablename__ = "Banks_Used"
    id = sa.Column(sa.Integer, primary_key=True)
    code = sa.Column(sa.Integer)
    codeOfCity = sa.Column(sa.Integer)
    name = sa.Column(sa.Text)
    nameOfCity = sa.Column(sa.Text)
    selfCode = sa.Column(sa.Integer)


#Банки
class Banks_Data(Base):
    __tablename__ = "Banks_Data"
    id = sa.Column(sa.Integer, primary_key=True)
    code = sa.Column(sa.Integer)
    name = sa.Column(sa.Text)


#Действия пользвателя
class User_Data_Action(Base):
    __tablename__ = "User_Data_Action"
    id = sa.Column(sa.Integer, primary_key=True)
    date = sa.Column(sa.Text) # Время
    codeM1 = sa.Column(sa.Integer) # код валюты номер 1
    codeM2 = sa.Column(sa.Integer)  # код валюты номер 2
    sizeSend = sa.Column(sa.Integer) # Количество проданной
    sizeGet = sa.Column(sa.Integer) # Количество купленной
    secondName = sa.Column(sa.Text)# Фамилия
    course = sa.Column(sa.Integer)# Курс
    codeB = sa.Column(sa.Integer)# Код банка
    selfCode = sa.Column(sa.Integer) # Свой код

