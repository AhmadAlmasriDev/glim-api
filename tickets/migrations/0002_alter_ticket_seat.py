# Generated by Django 3.2.23 on 2023-11-13 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='seat',
            field=models.IntegerField(),
        ),
    ]
