# Generated by Django 4.2.6 on 2023-10-20 06:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0003_cart_item_cart'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='cart',
            new_name='cartModel',
        ),
    ]
