from django.db.models import TextChoices


class OrderStatus(TextChoices):
    IN_PROCESS = ('in process', 'В процессе')
    PASSED = ('passed', 'прошел')
    CANCELLED = ('cancelled', 'отменен')
