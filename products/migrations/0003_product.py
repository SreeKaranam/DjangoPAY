# Generated by Django 2.2.2 on 2019-06-28 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20190628_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
                ('name', models.CharField(max_length=40)),
                ('company', models.CharField(max_length=30)),
                ('items', models.IntegerField()),
            ],
        ),
    ]