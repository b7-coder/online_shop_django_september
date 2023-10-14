from django.db import models
from .mixins import *
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
    