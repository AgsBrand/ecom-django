# Generated by Django 4.2.1 on 2023-09-07 07:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.CharField(default='Available', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 9, 7, 7, 14, 14, 836454, tzinfo=datetime.timezone.utc)),
        ),
    ]
