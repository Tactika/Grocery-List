# Generated by Django 3.1.5 on 2021-01-15 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocerylist', '0004_auto_20210113_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerylist',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
