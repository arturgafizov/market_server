from django.db import models

from apps.suppliers.models import Supplier, SupplierOrder


class Nomenclature(models.Model):
    name = models.CharField(max_length=256, null=True, verbose_name='Наименование')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='nomenclature_set')
    article_WB = models.CharField(max_length=256, null=True, verbose_name='Артикул WB')
    article_OZON = models.CharField(max_length=256, null=True, verbose_name='Артикул OZON')
    article_YA = models.CharField(max_length=256, null=True, verbose_name='Артикул YA')
    size = models.CharField(max_length=256, null=True, verbose_name='Размер')
    color = models.CharField(max_length=256, null=True, verbose_name='Цвет')
    barcode = models.CharField(max_length=30, null=True, verbose_name='Бар-код')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Стоимость')

    objects = models.Manager()

    def __str__(self):
        return f'#{self.pk} {self.name} {self.price}'


class Product(models.Model):
    number = models.CharField(max_length=256, null=True, verbose_name='Номер')
    code_product = models.CharField(max_length=256, null=True, verbose_name='Код продукта')
    quantity = models.PositiveIntegerField(null=True, verbose_name='Количество')
    price = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Стоимость')
    supplier_order = models.ForeignKey(SupplierOrder, on_delete=models.CASCADE, related_name='product_supplier_order')
    # sum =
    brand = models.CharField(max_length=50, null=True, verbose_name='Бренд')
    subject = models.CharField(max_length=50, null=True, verbose_name='Предмет')
    size_code = models.CharField(max_length=200, null=True, verbose_name='Код размера')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='product_supplier')
    nomenclature = models.ForeignKey(Nomenclature, on_delete=models.CASCADE, related_name='product_nomenclature')

    objects = models.Manager()

    def __str__(self):
        return f'#{self.pk} {self.subject} {self.price}'
