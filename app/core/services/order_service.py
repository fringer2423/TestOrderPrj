from ..models import Order


def get_order_list():
    """
    Функция для orm запроса всех заказов.
    :return: Список заказов
    """
    return Order.objects.all()
