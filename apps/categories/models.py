from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    # class CardiacClinic(models.model):
