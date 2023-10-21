from django.db import models
from .mixins import *
from django.conf import settings
"""
Категории
    Имя
    Картинка
    Описание
Бренды
    Имя
    Картинка
    Описание
Продукты
    Имя
    Описание
    Главная картинка
    Цена
    Цвета
    Вес
    Штрих код продукта
    
Картинки-Продуктов
    Продукт
    Картинка


Блоги(новости)
    Тема
    Текст
    Картинка
    Дата создания
    Автор
Работники
    ФИО
    Должность
    Автарка
Отзывы
    ФИО
    Должность
    Сообщение
    Аватарка
Заявки
    Имя
    Фамилия
    Номер
    Почта
    Сообщение
Корзина(для клиентов)
    Пользователь
    Продукт
    Количество
"""

class Contacts(TimestampMixin, models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    number = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    message = models.CharField(max_length=250)

class Workers(models.Model):
    fullname = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    avatar = models.ImageField()

class Reviews(models.Model):
    fullname = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    message = models.CharField(max_length=250)
    avatar = models.ImageField()


class Blogs(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

class Category(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=250)
class Brands(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=250)
class Products(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    image = models.ImageField()
    price = models.FloatField()
    color = models.CharField(max_length=250)
    weight = models.FloatField()
    barcode = models.CharField(max_length=250)
    categoryObject = models.ForeignKey(Category, on_delete=models.CASCADE)
    brandObject = models.ForeignKey(Brands, on_delete=models.CASCADE)

class ProductsImages(models.Model):
    productObject = models.ForeignKey(Products, on_delete=models.CASCADE)
    image = models.ImageField()
