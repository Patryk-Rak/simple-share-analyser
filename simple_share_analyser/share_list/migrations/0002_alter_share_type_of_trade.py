# Generated by Django 4.0.4 on 2022-04-25 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='type_of_trade',
            field=models.CharField(choices=[('Sold', 'Sold'), ('Bought', 'Bought')], max_length=6),
        ),
    ]
