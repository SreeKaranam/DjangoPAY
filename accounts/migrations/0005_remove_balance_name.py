# Generated by Django 2.2.2 on 2019-06-26 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_balance_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='name',
        ),
    ]
