import os
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.safestring import mark_safe

from .managers import UserManager


class User(AbstractUser):
    ADMIN = 'admin'
    ASSISTANT = 'assistant'
    ROLES = (
        (ADMIN, 'Админ'),
        (ASSISTANT, 'ассистент'),
    )

    email = models.EmailField(_('Email address'), unique=True)
    phone = PhoneNumberField(unique=True, null=True, blank=True, verbose_name='Мобильный телефон')
    role = models.CharField(max_length=128, choices=ROLES, default=ASSISTANT, verbose_name='Роль')
    middle_name = models.CharField(max_length=32, blank=True, null=True)
    position = models.CharField(max_length=128, null=True, blank=True, verbose_name='Должность')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        permissions = (
            ('assistant_access', 'Assistant'),
        )

    def __str__(self):
        return self.email

    @property
    def full_name(self):
        if self.middle_name is None:
            self.middle_name = ''
        if self.first_name is None:
            self.first_name = ''
        return f'{self.last_name} {self.first_name} {self.middle_name}'.strip()

    def user_active_quantity(self):
        users = User.objects.all()
        return users.filter(is_active=True).count()

    def delete(self, **kwargs):
        self.outstandingtoken_set.all().delete()
        return super().delete(**kwargs)

    @property
    def filename(self):
        return os.path.basename(self.full_name)


class IdentificationCode(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    code = models.CharField(_('Code'), max_length=10)
    active = models.BooleanField(_('Active'), default=True)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Time created'))
    objects = models.Manager()
