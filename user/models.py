from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                null=True, blank=True)
    name = models.CharField(verbose_name='Имя пользователя',
                            max_length=300,
                            blank=True,
                            help_text='Укажите имя пользователя')
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    description = models.TextField('Описание к профилю',
                                   max_length=300,
                                   blank=True,
                                   help_text='Укажите описание')
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['name']
