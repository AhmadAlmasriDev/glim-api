# Generated by Django 3.2.23 on 2024-01-03 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20231113_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
