# Generated by Django 3.1.5 on 2021-01-13 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocerylist', '0002_auto_20210112_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grocerylist',
            name='completed_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
