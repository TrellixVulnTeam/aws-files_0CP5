# Generated by Django 3.0 on 2020-04-01 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_pizza_topping'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='spicy',
            field=models.CharField(default=True, max_length=30),
        ),
    ]
