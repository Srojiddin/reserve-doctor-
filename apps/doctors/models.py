# from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from apps.categories.models import Category





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



# class DoctorProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     specialization = models.CharField(max_length=100)
#     education = models.CharField(max_length=200)
#     experience = models.IntegerField()
#     contact_info = models.CharField(max_length=200)

#     def __str__(self):
#         return self.user.username