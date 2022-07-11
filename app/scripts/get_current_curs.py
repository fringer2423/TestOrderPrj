import time
import requests
import xmltodict
import db_support


def set_curs_to_db():
    """
    Функция обновляющая курс валют
    :return: null
    """
    db_support.update_curs(get_curs())


def get_curs(id='R01235'):
    """
    Функция получает курс от ЦБ РФ.
    :param id: id нужной валюты.
    :return: текущий курс по ЦБ РФ.
    """
    url = "https://www.cbr.ru/scripts/XML_daily.asp?id=R01235"

    resp = requests.get(url)

    print(resp.status_code)
    valCurs = xmltodict.parse(resp.content)
    valCurs = valCurs['ValCurs']['Valute']

    currentCurs = list(filter(lambda item: item['@ID'] == id, valCurs))[0]['Value']
    currentCurs = currentCurs.replace(',', '.')
    return currentCurs


def run():
    set_curs_to_db()


if __name__ == '__main__':
    while True:
        try:
            time.sleep(1800)
            run()
        except Exception as error:
            print(error)
