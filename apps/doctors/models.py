from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from apps.categories.models import Category

from apps.users.models import AbstractUser


class Doctor(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Имя"
    )
    choosing_a_specialization = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Выберите специализацию",
    )
    image_for_doctor = models.ImageField(
        upload_to="doctors_media/",
        verbose_name="Фото",
    )
    phone_number = models.CharField(
        max_length=15,
    )
    email = models.CharField(
        max_length=100,
    )
    creation_date = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата создания"
    )

    class Meta:
        verbose_name = "Доктор "
        verbose_name_plural = "Докторы"

    def __str__(self):
        return self.name

#
# class DoctorProfile(models.Model):
#     user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='doctor_profile')
#     doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE, related_name='profile')
#     bio = models.TextField(blank=True)
#     address = models.CharField(max_length=255, blank=True)
#     phone_number = models.CharField(max_length=20, blank=True)
#
#     def __str__(self):
#         return f"Profile of {self.user.username}"
