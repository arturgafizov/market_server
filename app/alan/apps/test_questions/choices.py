from django.db.models import TextChoices


class TestType(TextChoices):
    INTRODUCTORY = ('introductory', 'Вводный')
    EVERY_SHIFT = ('every_shift', 'Ежесменный')
    REPEATED = ('repeated', 'Повторный')
    THEMATIC = ('thematic', 'Тематический')
