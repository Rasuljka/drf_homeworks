from django.db import models


class Course(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Название курса",
        help_text="Укажите название курса",
    )
    image = models.ImageField(
        upload_to="materials/images",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью",
    )
    description = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Опишите курс",
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Название урока",
        help_text="Укажите название урока",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        help_text="Выберите курс",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="materials/images",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите превью",
    )
    description = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Описание",
        help_text="Опишите урок",
    )
    video = models.TextField(
        verbose_name="Видео урока",
        help_text="Загрузите видео урока",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
