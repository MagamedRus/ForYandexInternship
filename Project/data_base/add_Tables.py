from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
DB_PATH = "sqlite:///data_base.sqlite3"

meta = MetaData()
engine = create_engine('sqlite:///data_base.sqlite3', echo=True)


def engine_session():
    engine = sa.create_engine(DB_PATH)
    sessions = sessionmaker(engine)
    session = sessions()
    return session


# User_Data_Action = Table(
#     "User_Data_Action", meta,
#     Column("id", Integer, primary_key=True),
#     Column("date", Text),
#     Column("codeM1", Integer),
#     Column("codeM2", Integer),
#     Column("sizeSend", Integer),
#     Column("sizeGet", Integer),
#     Column("secondName", Text),
#     Column("course", Integer),
#     Column("codeB", Integer),
#     Column("selfCode", Integer)
# )


# User_Passport = Table(
#     "User_Passport", meta,
#     Column("id", Integer, primary_key=True),
#     Column("firstName", Text),
#     Column("secondName", Text),
#     Column("lastName", Text),
#     Column("sex", Text),
#     Column("birthday", Text),
#     Column("dateOfGet", Text),
#     Column("codeOfReg", Integer),
#     Column("birthPlace", Text),
#     Column("serial", Integer),
#     Column("number", Integer),
# )

#
# Exchange_Date = Table(
#     "Exchange_Date", meta,
#     Column("id", Integer, primary_key=True),
#     Column("code", Integer),
#     Column("codeA", Text),
#     Column("units", Integer),
#     Column("name", Text),
#     Column("course", Integer)
# )


# Each_City = Table(
#     "Each_City", meta,
#     Column("id", Integer, primary_key=True),
#     Column("code", Integer),
#     Column("name", Text)
# )


# City = Table(
#     "City", meta,
#     Column("id", Integer, primary_key=True),
#     Column("code", Integer),
#     Column("name", Text)
# )

# Banks_Used = Table(
#     "Banks_Used", meta,
#     Column("id", Integer, primary_key=True),
#     Column("code", Integer),
#     Column("name", Text),
#     Column("codeOfCity", Integer),
#     Column("nameOfCity", Text),
#     Column("actCode", Integer)
# )


# Banks_data = Table(
#     "Banks_Data", meta,
#     Column("id", Integer, primary_key=True),
#     Column("code", Integer),
#     Column("name", Text),
# )
meta.create_all(engine)