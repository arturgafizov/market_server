from django.db import models

# Create your models here.


class Warehouse(models.Model):
    name = models.CharField(max_length=256, null=True, verbose_name='Название склада')
    code = models.CharField(max_length=256, null=True, verbose_name='Код склада')

    objects = models.Manager()

    def __str__(self):
        return f'#{self.pk} {self.name} {self.code}'


