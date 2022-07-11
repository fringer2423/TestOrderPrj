import db_support
from get_current_curs import get_curs


def run():
    """
    Функция выполняется при сборке контейнера и вызывает функцию создания таблицы для курса валют.
    :return: null
    """
    db_support.create_table_curs(get_curs())


if __name__ == '__main__':
    run()
