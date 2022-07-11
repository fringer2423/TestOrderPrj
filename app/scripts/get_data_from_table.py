import os
import time
import gspread
import pandas as pd
import db_support

from oauth2client.service_account import ServiceAccountCredentials as sac


def add_df_to_DB(df):
    """
    Функция переносит данные из pandas в базу данных
    :param df: Pandas таблица
    :return: null
    """
    engine = db_support.get_db_engine()

    connection = engine.connect()

    df.to_sql('order', con=engine, if_exists='replace', index=True, schema="public", index_label='id')

    connection.execute('grant select on public.order to test; ALTER TABLE "order" ADD PRIMARY KEY ("id");')

    connection.close()


def add_cost_to_df(df, current_curs):
    """
    Функция добавляет в таблицу pandas столбец со стоимостью в рублях
    :param df: pandas таблица
    :param current_curs: текущий курс
    :return: null
    """
    data = list()
    for row in df.itertuples(index=False):
        item = round(float(row[2]) * current_curs)
        data.append(item)
    df.insert(loc=df.shape[1], column='стоимость, руб', value=data, allow_duplicates=False)


def gsheet_to_df(spreadsheet_name, sheet_num):
    """
    Функция получает данные из google таблицы, и переносит их в pandas
    :param spreadsheet_name: Имя таблицы google
    :param sheet_num: Номер таблицы
    :return: Pandas таблица с данными
    """
    scope = ['https://spreadsheets.google.com/feeds']
    credentials_path = '/usr/src/app/scripts/creds.json'

    credentials = sac.from_json_keyfile_name(credentials_path, scope)
    client = gspread.authorize(credentials)

    sheet = client.open_by_key(spreadsheet_name).get_worksheet(sheet_num).get_all_records()
    df = pd.DataFrame.from_dict(sheet)

    return df


def run():
    """
    Основная функция, которая получает название таблицы и вызывает остальные функции.
    :return: null
    """

    sheet_key = os.environ.get('SHEET_KEY')
    order_df = gsheet_to_df(sheet_key, 0)

    current_curs = db_support.get_curs()

    add_cost_to_df(order_df, current_curs)

    add_df_to_DB(order_df)


if __name__ == '__main__':
    while True:
        try:
            time.sleep(30)
            run()
        except Exception as error:
            print(error)
