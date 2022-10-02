from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from .choices import OrderStatus
from ..warehouses.models import Warehouse

User = get_user_model()


class Supplier(models.Model):
    name = models.CharField(max_length=256, null=True, verbose_name='Наименование поставщика')
    country = models.CharField(max_length=256, null=True, verbose_name='Страна')
    city = models.CharField(max_length=256, null=True, verbose_name='Город')
    address = models.CharField(max_length=256, null=True, verbose_name='Адрес')
    phone = PhoneNumberField(unique=True, null=True, blank=True, verbose_name='Мобильный телефон')
    email = models.EmailField(_('Email address'), unique=True)
    site = models.CharField(max_length=256, null=True, verbose_name='Сайт')
    supplier_code = models.CharField(max_length=256, null=True, verbose_name='Код поставщика')
    article_delivery = models.CharField(max_length=256, null=True, verbose_name='Артикул поставщика')
    # product_category = models.CharField(max_length=256, null=True, verbose_name='Категория товаров')

    objects = models.Manager()

    def __str__(self):
        return f'#{self.pk} {self.name}'


class SupplierOrder(models.Model):
    number_document = models.CharField(max_length=256, null=True, verbose_name='Номер документа')
    date_application = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата заявки')
    link_to_document = models.URLField(null=True, verbose_name='Ссылка на документ')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='supplier_order_warehouse')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplier_order')
    sum = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Сумма')
    note = models.CharField(max_length=256, null=True, verbose_name='Примечание')
    # employee = models.CharField(max_length=256, null=True, verbose_name='Сотрудник')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='supplier_order_user')
    status = models.CharField(choices=OrderStatus.choices, max_length=50, default=OrderStatus.IN_PROCESS)
    date_completion = models.DateTimeField(auto_now_add=True, verbose_name='Дата выполнение')
    added = models.CharField(max_length=256, null=True, verbose_name='Добавлено')
    code_application = models.CharField(max_length=100, null=True, verbose_name='Код заявки')

    objects = models.Manager()

    def __str__(self):
        return f'#{self.pk} {self.number_document} {self.sum}'
