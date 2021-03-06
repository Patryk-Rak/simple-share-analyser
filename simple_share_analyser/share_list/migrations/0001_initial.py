# Generated by Django 4.0.4 on 2022-04-25 22:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('price', models.IntegerField()),
                ('transaction_date', models.DateTimeField(default=datetime.datetime.now)),
                ('type_of_trade', models.CharField(choices=[('S', 'Sold'), ('B', 'Bought')], max_length=1)),
            ],
        ),
    ]
