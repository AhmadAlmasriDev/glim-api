# Generated by Django 3.2.23 on 2024-01-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_alter_ticket_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='purchased',
            field=models.BooleanField(default=False),
        ),
    ]
