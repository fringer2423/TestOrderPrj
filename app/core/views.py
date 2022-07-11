from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import OrderSerializer
from .services.order_service import get_order_list


class OrderListView(APIView):
    """
    Контроллер для вывода списка заказов
    """
    def get(self, request):
        serializer = OrderSerializer(get_order_list(), many=True)
        return Response(serializer.data)
