# Generated by Django 3.2.9 on 2021-11-11 08:31

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpItem',
            fields=[
                ('number', models.CharField(help_text='Укажите номер объекта ИС', max_length=15, verbose_name='Номер объекта ИС')),
                ('title', models.CharField(blank=True, help_text='Напишите название объекта ИС', max_length=200, verbose_name='Название объекта ИС')),
                ('type_of_item', models.CharField(choices=[('PM', 'полезная модель'), ('IZ', 'изобретение'), ('PO', 'промышленный образец')], default='PM', max_length=2, verbose_name='Тип объекта ИС')),
                ('initial_date', models.DateField(blank=True, default=datetime.date.today, help_text='Укажите дату', verbose_name='Дата начала действия')),
                ('description', models.TextField(blank=True, help_text='Описание объекта ИС', max_length=300, verbose_name='Опишите объект ИС')),
                ('signatory', models.CharField(default='', help_text='В формате ФИО или Директор ООО "Рога и копыта" ФИО', max_length=15, verbose_name='Подписант')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
            options={
                'ordering': ['number'],
            },
        ),
    ]
