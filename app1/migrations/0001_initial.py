# Generated by Django 4.2.6 on 2023-10-17 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_available',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=255, null=True)),
                ('pro_price', models.IntegerField(null=True)),
                ('pro_description', models.CharField(max_length=300, null=True)),
                ('pro_image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
    ]
