from django.contrib.auth.models import User

from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )

    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )

    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='user_pics',
        verbose_name='Аватар'
    )

    about_me = models.TextField(
        null = True,
        blank=True,
        max_length=1000,
        verbose_name='О себе'
    )

    github_link = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name='GitHub'
    )

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


