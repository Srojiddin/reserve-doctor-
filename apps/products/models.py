import os
from django.db import models
from django.urls import reverse


class Medicine(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Название",
    )
    # description = models.TextField(
    #     verbose_name="Описание",
    #     blank=True,
    #     null=None,
    # )
    image_for_medicine = models.ImageField(
        upload_to='medicine/',
        blank=True,
        null=True,
        verbose_name="Картинка",
    )
    price_for_medicine = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создание",
    )


    def __str__(self):
        return self.name


class Shop(models.Model):
    ...


# class ShopSingle(models.Model):
#     ...
#
