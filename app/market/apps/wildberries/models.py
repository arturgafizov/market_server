from django.db import models

from .choices import TypeDocument
# Create your models here.


class WBOrder(models.Model):
    date = models.DateTimeField(null=True, verbose_name='Дата и время продажи')
    lastChangeDate = models.DateTimeField(null=True, verbose_name='Дата и время обновления информации')
    supplierArticle = models.CharField(max_length=75, null=True, verbose_name='Артикул поставщика')
    techSize = models.CharField(max_length=30, null=True, verbose_name='Размер')
    barcode = models.CharField(max_length=30, null=True, verbose_name='Бар-код')
    totalPrice = models.DecimalField(max_digits=11, decimal_places=2,
                                     verbose_name='Цена до согласованной скидки/промо/спп')
    discountPercent = models.PositiveIntegerField(null=True, verbose_name='Согласованный итоговый дисконт')
    warehouseName = models.CharField(max_length=50, null=True, verbose_name='Название склада отгрузки')
    oblast = models.CharField(max_length=200, null=True, verbose_name='Область')
    incomeID = models.IntegerField(null=True, verbose_name='Номер поставки')
    odid = models.BigIntegerField(null=True, verbose_name='Уникальный идентификатор позиции заказа')
    nmId = models.IntegerField(null=True, verbose_name='Код WB')
    subject = models.CharField(max_length=50, null=True, verbose_name='Предмет')
    category = models.CharField(max_length=50, null=True, verbose_name='Категория')
    brand = models.CharField(max_length=50, null=True, verbose_name='Бренд')
    isCancel = models.BooleanField(default=False, verbose_name='Отмена заказа')
    cancel_dt = models.DateTimeField(null=True, verbose_name='Дата и время отмены заказа')
    gNumber = models.CharField(max_length=50, null=True, verbose_name='Номер заказа')
    sticker = models.CharField(max_length=256, null=True, verbose_name='Цифровое значение стикера')
    srid = models.CharField(max_length=256, null=True, verbose_name='Уникальный идентификатор заказа')

    objects = models.Manager()

    def __str__(self):
        return f'#{self.pk} {self.subject} {self.srid}'


class WBSell(models.Model):
    date = models.DateTimeField(null=True, verbose_name='Дата и время продажи')
    lastChangeDate = models.DateTimeField(null=True, verbose_name='Дата и время обновления информации')
    supplierArticle = models.CharField(max_length=75, null=True, verbose_name='Артикул поставщика')
    techSize = models.CharField(max_length=30, null=True, verbose_name='Размер')
    barcode = models.CharField(max_length=30, null=True, verbose_name='Бар-код')
    totalPrice = models.DecimalField(max_digits=11, decimal_places=2,
                                     verbose_name='Цена до согласованной скидки/промо/спп')
    discountPercent = models.PositiveIntegerField(null=True, verbose_name='Согласованный итоговый дисконт')
    isSupply = models.BooleanField(default=False, verbose_name='Договор поставки')
    isRealization = models.BooleanField(default=True, verbose_name='Договор реализации')
    promoCodeDiscount = models.PositiveIntegerField(default=0, verbose_name='Скидка по промокоду')
    warehouseName = models.CharField(max_length=50, null=True, verbose_name='Название склада отгрузки')
    countryName = models.CharField(max_length=200, null=True, verbose_name='Страна')
    oblastOkrugName = models.CharField(max_length=200, null=True, verbose_name='Округ')
    regionName = models.CharField(max_length=200, null=True, verbose_name='Регион')
    incomeID = models.IntegerField(null=True, verbose_name='Номер поставки')
    odid = models.BigIntegerField(null=True, verbose_name='Уникальный идентификатор позиции заказа')
    spp = models.IntegerField(default=0, verbose_name='Согласованная скидка постоянного покупателя')
    forPay = models.DecimalField(max_digits=11, decimal_places=2, null=True, verbose_name='К перечислению')
    finishedPrice = models.DecimalField(max_digits=11, decimal_places=2, null=True,
                                        verbose_name='актическая цена заказа')
    priceWithDisc = models.DecimalField(max_digits=11, decimal_places=2, null=True,
                                        verbose_name='Цена, от которой считается вознаграждение поставщика')
    nmId = models.IntegerField(null=True, verbose_name='Код WB')
    subject = models.CharField(max_length=50, null=True, verbose_name='Предмет')
    category = models.CharField(max_length=50, null=True, verbose_name='Категория')
    brand = models.CharField(max_length=50, null=True, verbose_name='Бренд')
    IsStorno = models.IntegerField(default=0, verbose_name='Cторно операция')
    gNumber = models.CharField(max_length=50, null=True, verbose_name='Номер заказа')
    sticker = models.CharField(max_length=256, null=True, verbose_name='Цифровое значение стикера')
    srid = models.CharField(max_length=256, null=True, verbose_name='Уникальный идентификатор заказа')

    objects = models.Manager()

    def __str__(self):
        return f'#{self.pk} {self.subject} {self.srid}'


class WBStock(models.Model):
    lastChangeDate = models.DateTimeField(null=True, verbose_name='Дата и время обновления информации')
    techSize = models.CharField(max_length=30, null=True, verbose_name='Размер')
    barcode = models.CharField(max_length=30, null=True, verbose_name='Бар-код')
    quantity = models.IntegerField(null=True, verbose_name='Количество')
    isSupply = models.BooleanField(default=False, verbose_name='Договор поставки')
    isRealization = models.BooleanField(default=True, verbose_name='Договор реализации')
    warehouse = models.IntegerField(null=True, verbose_name='Уникальный идентификатор склада')
    warehouseName = models.CharField(max_length=50, null=True, verbose_name='Название склада отгрузки')
    inWayToClient = models.IntegerField(null=True, verbose_name='В пути к клиенту')
    inWayFromClient = models.IntegerField(null=True, verbose_name='В пути от клиента')
    nmId = models.IntegerField(null=True, verbose_name='Код WB')
    subject = models.CharField(max_length=50, null=True, verbose_name='Предмет')
    category = models.CharField(max_length=50, null=True, verbose_name='Категория')
    brand = models.CharField(max_length=50, null=True, verbose_name='Бренд')
    SCCode = models.CharField(max_length=50, null=True, verbose_name='Код контракта')
    Price = models.DecimalField(max_digits=11, decimal_places=2, null=True, verbose_name='Цена')
    Discount = models.PositiveIntegerField(null=True, verbose_name='Скидка')

    objects = models.Manager()

    def __str__(self):
        return f'#{self.pk} {self.subject} {self.nmId}'


class WBReportDetailByPeriod(models.Model):
    realizationreport_id = models.IntegerField(verbose_name='Номер отчета')
    date_from = models.DateTimeField(null=True, verbose_name='Дата начала отчетного периода')
    date_to = models.DateTimeField(null=True, verbose_name='Дата конца отчетного периода')
    suppliercontract_code = models.CharField(max_length=256, null=True, verbose_name='Договор')
    rrd_id = models.BigIntegerField(null=True, verbose_name='Номер строки')
    gi_id = models.BigIntegerField(null=True, verbose_name='Номер поставки')
    subject_name = models.CharField(max_length=256, null=True, verbose_name='Предмет')
    nm_id = models.BigIntegerField(null=True, verbose_name='Артикул')
    brand_name = models.CharField(max_length=256, null=True, verbose_name='Бренд')
    sa_name = models.CharField(max_length=256, null=True, verbose_name='Артикул поставщика')
    ts_name = models.CharField(max_length=256, null=True, verbose_name='Размер')
    barcode = models.CharField(max_length=30, null=True, verbose_name='Бар-код')
    doc_type_name = models.CharField(choices=TypeDocument.choices, max_length=50)
    quantity = models.IntegerField(null=True, verbose_name='Количество')
    retail_price = models.IntegerField(null=True, verbose_name='Цена розничная')
    retail_amount = models.IntegerField(null=True, verbose_name='Сумма продаж')
    sale_percent = models.PositiveIntegerField(null=True, verbose_name='Согласованная скидка')
    commission_percent = models.PositiveIntegerField(null=True, verbose_name='Процент комиссии')
    office_name = models.CharField(max_length=256, null=True, verbose_name='Склад')
    supplier_oper_name = models.CharField(max_length=256, null=True, verbose_name='Обоснование для оплаты')
    order_dt = models.DateTimeField(null=True, verbose_name='Дата заказа')
    sale_dt = models.DateTimeField(null=True, verbose_name='Дата продажи')
    rr_dt = models.DateTimeField(null=True, verbose_name='Дата операции')
    shk_id = models.BigIntegerField(null=True, verbose_name='Штрих-код')
    retail_price_withdisc_rub = models.DecimalField(max_digits=11, decimal_places=2, null=True,
                                                    verbose_name='Цена розничная с учетом согласованной скидки')
    delivery_amount = models.IntegerField(null=True, verbose_name='Количество доставок')
    return_amount = models.IntegerField(null=True, verbose_name='Количество возвратов')
    delivery_rub = models.DecimalField(max_digits=11, decimal_places=2, null=True, verbose_name='Стоимость логистики')
    gi_box_type_name = models.CharField(max_length=256, null=True, verbose_name='Тип коробов')
    product_discount_for_report = models.PositiveIntegerField(null=True,
                                                              verbose_name='Согласованный продуктовый дисконт')
    supplier_promo = models.IntegerField(null=True, verbose_name='Промокод')
    rid = models.BigIntegerField(null=True, verbose_name='Уникальный идентификатор позиции заказа')
    ppvz_spp_prc = models.PositiveIntegerField(null=True, verbose_name='Скидка постоянного покупателя')
    ppvz_kvw_prc_base = models.PositiveIntegerField(null=True, verbose_name='Размер кВВ без НДС, % базовый')
    ppvz_kvw_prc = models.PositiveIntegerField(null=True, verbose_name='Итоговый кВВ без НДС, %')
    ppvz_sales_commission = models.IntegerField(null=True, verbose_name='Вознаграждение с продаж до вычета услуг '
                                                                        'поверенного, без НДС')
    ppvz_for_pay = models.DecimalField(max_digits=11, decimal_places=2, null=True, verbose_name='К перечислению продавцу '
                                                                                               'за реализованный товар')
    ppvz_reward = models.DecimalField(max_digits=11, decimal_places=2, null=True, verbose_name='Возмещение расходов '
                                                                                               'услуг поверенного')
    ppvz_vw = models.DecimalField(max_digits=11, decimal_places=2, null=True, verbose_name='Вознаграждение WB без НДС')
    ppvz_vw_nds = models.DecimalField(max_digits=11, decimal_places=2, null=True, verbose_name='НДС с вознаграждения '
                                                                                               'WB')
    ppvz_office_id = models.IntegerField(null=True, verbose_name='Номер офиса')
    ppvz_office_name = models.CharField(max_length=256, null=True, verbose_name='Наименование офиса доставки')
    ppvz_supplier_id = models.IntegerField(null=True, verbose_name='Номер партнера')
    ppvz_supplier_name = models.CharField(max_length=256, null=True, verbose_name='Партнер')
    ppvz_inn = models.CharField(max_length=256, null=True, verbose_name='ИНН партнера')
    declaration_number = models.CharField(max_length=256, null=True, verbose_name='Номер таможенной декларации')
    sticker_id = models.CharField(max_length=256, null=True, verbose_name='Цифровое значение стикера')
    site_country = models.CharField(max_length=256, null=True, verbose_name='Страна продажи')
    penalty = models.DecimalField(max_digits=11, decimal_places=2, null=True, default=0, verbose_name='Штраф')
    additional_payment = models.DecimalField(max_digits=11, decimal_places=2, null=True, default=0, verbose_name='Доплата')
    srid = models.CharField(max_length=256, null=True, verbose_name='Уникальный идентификатор заказа')

    objects = models.Manager()

    def __str__(self):
        return f'#{self.pk} {self.subject_name} {self.srid}'


class WBFinancialReport(models.Model):
    report_number = models.CharField(max_length=256, null=True, verbose_name='Номер отчета')
    date_start = models.DateTimeField(null=True, verbose_name='Дата начала')
    date_end = models.DateTimeField(null=True, verbose_name='Дата окончания')
    date_formations = models.DateTimeField(null=True, verbose_name='Дата формирования')
    sale = models.DecimalField(max_digits=11, decimal_places=2, null=True, verbose_name='Продажа')
    agreed_discount = models.PositiveIntegerField(null=True, verbose_name='Согласованная скидка')
    to_paid = models.DecimalField(max_digits=11, decimal_places=2, null=True, verbose_name='К оплате за товар')
    cost_logistics = models.DecimalField(max_digits=11, decimal_places=2, null=True, verbose_name='Стоимость логистики')
    fine = models.DecimalField(max_digits=11, decimal_places=2, null=True, verbose_name='Штраф')
