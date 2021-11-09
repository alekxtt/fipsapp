from django.db import models
from user.models import Profile
import uuid
import datetime


class IpItem(models.Model):
    UTILITY_MODEL = 'PM'
    INVENTION = 'IZ'
    DESIGN = 'PO'
    ITEMS_FOR_CHOICE = [
        (UTILITY_MODEL, 'полезная модель'),
        (INVENTION, 'изобретение'),
        (DESIGN, 'промышленный образец'),
    ]
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    number = models.CharField(verbose_name='Номер объекта ИС',
                              max_length=15,
                              help_text='Укажите номер объекта ИС')
    title = models.CharField(verbose_name='Название объекта ИС',
                             max_length=200,
                             blank=True,
                             help_text='Напишите название объекта ИС')
    type_of_item = models.CharField(verbose_name='Тип объекта ИС',
                                    max_length=2,
                                    choices=ITEMS_FOR_CHOICE,
                                    default=UTILITY_MODEL)
    initial_date = models.DateField('Дата начала действия',
                                    default=datetime.date.today,
                                    blank=True,
                                    help_text='Укажите дату')
    description = models.TextField('Опишите объект ИС',
                                   max_length=300,
                                   blank=True,
                                   help_text='Описание объекта ИС')
    signatory = models.CharField(verbose_name='Подписант',
                                 default='',
                                 max_length=15,
                                 help_text='В формате ФИО или Директор ООО "Рога и копыта" ФИО')
    id = models.UUIDField(default=uuid.uuid4,
                          unique=True,
                          primary_key=True,
                          editable=False)

    def __str__(self):
        return self.number

    class Meta:
        ordering = ['number']
