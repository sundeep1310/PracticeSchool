# Generated by Django 5.0.3 on 2024-03-31 11:04

import account.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', account.models.CustomUserManager()),
            ],
        ),
    ]
