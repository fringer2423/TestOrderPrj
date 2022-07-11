import os
import sqlalchemy as sa
import psycopg2
from enum import Enum



__DATABASE = os.environ.get('SQL_DATABASE')
__USER = os.environ.get('SQL_USER')
__PASSWORD = os.environ.get('SQL_PASSWORD')
__HOST = os.environ.get('SQL_HOST')
__PORT = os.environ.get('SQL_PORT')


def get_db_engine():
    """
    Функция, возвращающая engine для sqlalchemy
    :return: engine для sqlalchemy
    """
    connection_string = "postgresql+psycopg2://%s:%s@%s:%s/%s" % (__USER,
                                                                  __PASSWORD,
                                                                  __HOST,
                                                                  __PORT,
                                                                  __DATABASE)
    engine = sa.create_engine(connection_string)
    return engine


def get_connect_to_db():
    """
    Функция, возвращающая connect к базе данных
    :return: connect
    """
    con = psycopg2.connect(
        database=__DATABASE,
        user=__USER,
        password=__PASSWORD,
        host=__HOST,
        port=__PORT
    )

    return con


def create_table_curs(curs):
    """
    Функция создающая таблицу для хранения курса валют
    :param curs: значение курса
    :return: null
    """
    con = None
    cur = None
    try:
        con = get_connect_to_db()
        cur = con.cursor()
        cur.execute('''CREATE TABLE CURS
             (ID INT PRIMARY KEY NOT NULL,
             VALUE FLOAT NOT NULL);''')

        con.commit()

        cur.execute("INSERT INTO CURS (ID,VALUE) VALUES (%s, %s)", (1, curs,))
        con.commit()
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if con:
            cur.close()
            con.close()


def update_curs(curs):
    """
    Функция, обновляющая значение курса в базе данных
    :param curs: значение курса
    :return: null
    """
    con = None
    cur = None
    try:
        con = get_connect_to_db()
        cur = con.cursor()

        cur.execute("UPDATE CURS set VALUE = %s where ID = 1", (curs,))
        con.commit()
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if con:
            cur.close()
            con.close()


def get_curs():
    """
    Функция возвращающая текущий курс из базы данных.
    :return: текущий курс
    """
    con = None
    cur = None
    try:
        con = get_connect_to_db()
        cur = con.cursor()

        cur.execute("SELECT VALUE from CURS")
        curs = cur.fetchall()[0][0]
        return curs
    except (Exception, psycopg2.Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if con:
            cur.close()
            con.close()
