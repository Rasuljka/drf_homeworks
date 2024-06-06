from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


class User(AbstractUser):

    username = None

    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Укажите почту"
    )

    phone = models.CharField(
        max_length=35,
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Укажите телефон",
    )
    tg_nick = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Телеграмм",
        help_text="Укажите телеграмм",
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        verbose_name="Аватар",
        help_text="Загрузите аватар",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payments(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="пользователь"
    )
    pay_date = models.DateTimeField(auto_now=True, verbose_name="дата оплаты")
    paid_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="оплаченный курс",
        blank=True,
        null=True,
    )
    paid_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="оплаченный урок",
        blank=True,
        null=True,
    )
    pay_sum = models.PositiveIntegerField(verbose_name="сумма оплаты")
    pay_transfer = models.BooleanField(default=True, verbose_name="оплата переводом")

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"
