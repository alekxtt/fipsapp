from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import IpItem


class DateInput(forms.DateInput):
    input_type = 'date'


class IpItemForm(ModelForm):
    class Meta:
        model = IpItem
        fields = ['number', 'title', 'type_of_item', 'initial_date',
                  'description', 'signatory']
        labels = {
            'number': 'Номер патента/товарного знака',
            'title': 'Название',
            'type_of_item': 'Тип объекта',
            'initial_date': 'Дата начала действия патента/товарного знака',
            'description': 'Описание',
            'signatory': 'Подписант',
        }
        widgets = {'initial_date': DateInput()}
