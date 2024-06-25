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
    owner = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Владелец",
        help_text="Укажите владельца",
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='Владелец',
        blank=True,
        null=True,
    )
    course = models.ForeignKey(
        'materials.Course',
        on_delete=models.CASCADE,
        verbose_name='Курс'
    )

    def __str__(self):
        return f'{self.user} - {self.course}'

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
