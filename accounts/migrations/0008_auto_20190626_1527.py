# Generated by Django 2.2.2 on 2019-06-26 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0007_auto_20190626_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='generated unique id for user', primary_key=True, serialize=False)),
                ('typeaccount', models.CharField(choices=[('1', 'Savings'), ('2', 'Current')], help_text='type of account', max_length=100, null=True)),
                ('balance', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['person_name'],
            },
        ),
        migrations.DeleteModel(
            name='balance',
        ),
        migrations.AddField(
            model_name='account',
            name='AccountUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Person'),
        ),
    ]
