import os
from django.db import models


class Speciality(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Специальность')
    objects = models.Manager()

    def __str__(self):
        return f'#{self.pk} {self.name}'


class Category(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Категория')
    code = models.CharField(max_length=128, blank=False, null=False, verbose_name='Код категории')
    objects = models.Manager()

    def __str__(self):
        return f'#{self.pk} {self.name}'


class Document(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Документ')
    file = models.FileField(upload_to='documents/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories',
                                 verbose_name='Категория')
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='specialities',
                                   verbose_name='Специальность')

    objects = models.Manager()

    @property
    def filename(self):
        return os.path.basename(self.file.name)


class Information(models.Model):
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    name = models.CharField(max_length=128, blank=False, null=False, verbose_name=' Информационный лист')
    file = models.FileField(upload_to='information/', blank=True)

    objects = models.Manager()

    @property
    def filename(self):
        return os.path.basename(self.file.name)
