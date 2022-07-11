# Generated by Django 4.0.6 on 2022-07-10 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('number', models.BigIntegerField(blank=True, db_column='№', null=True)),
                ('order_number', models.BigIntegerField(blank=True, db_column='заказ №', null=True)),
                ('cost_in_usd', models.BigIntegerField(blank=True, db_column='стоимость,$', null=True)),
                ('delivery_date', models.TextField(blank=True, db_column='срок поставки', null=True)),
                ('cost_in_rub', models.BigIntegerField(blank=True, db_column='стоимость, руб', null=True)),
            ],
            options={
                'db_table': 'order',
                'managed': False,
            },
        ),
    ]
