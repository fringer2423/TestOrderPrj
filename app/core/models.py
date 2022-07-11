from django.db import models


class Order(models.Model):
    """
    Модель заказа
    """
    id = models.BigIntegerField(primary_key=True)
    number = models.BigIntegerField(db_column='№', blank=True, null=True)
    order_number = models.BigIntegerField(db_column='заказ №', blank=True, null=True)
    cost_in_usd = models.BigIntegerField(db_column='стоимость,$', blank=True, null=True)
    delivery_date = models.TextField(db_column='срок поставки', blank=True, null=True)
    cost_in_rub = models.BigIntegerField(db_column='стоимость, руб', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'

    def __str__(self):
        return f'Заказ: {self.order_number} от {self.delivery_date}'
