# Generated by Django 3.2.23 on 2023-11-08 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='../default_profile_br7153', upload_to='images/'),
        ),
    ]
