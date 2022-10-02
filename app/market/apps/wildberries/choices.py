from django.db.models import TextChoices


class TypeDocument(TextChoices):
    SALE = ('sale', 'Продажа')
    RETURN = ('return', 'Возврат')
