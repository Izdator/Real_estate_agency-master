from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=200, db_index=True)
    phone_number = PhoneNumberField('Номер владельца', blank=True, null=True, db_index=True)
    flats = models.ManyToManyField('Flat', related_name='owners_set', verbose_name='Квартиры', blank=True)

    def __str__(self):
        return self.name


class Flat(models.Model):
    owners = models.ManyToManyField(Owner, related_name='owned_flats', verbose_name='Владельцы', blank=True)
    created_at = models.DateTimeField('Когда создано объявление', default=timezone.now, db_index=True)
    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)
    town = models.CharField('Город', max_length=50, db_index=True)
    town_district = models.CharField('Район', max_length=50, blank=True, help_text='Чертаново Южное')
    address = models.TextField('Адрес', help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField('Этаж', max_length=3, help_text='Первый этаж, последний этаж, пятый этаж')
    rooms_number = models.IntegerField('Количество комнат', db_index=True)
    living_area = models.IntegerField('Жилая площадь', null=True, blank=True, db_index=True)
    has_balcony = models.BooleanField('Наличие балкона', default=False, db_index=True)  # Установлено значение по умолчанию
    active = models.BooleanField('Активно', db_index=True)
    construction_year = models.IntegerField('Год постройки', null=True, blank=True, db_index=True)
    new_building = models.BooleanField('Новостройка', null=True, blank=True, db_index=True)
    liked_by = models.ManyToManyField(User, related_name='liked_flats', verbose_name='Кто лайкнул', blank=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    user = models.ForeignKey(User, related_name='complaints', on_delete=models.CASCADE, verbose_name='Кто жаловался')
    flat = models.ForeignKey(Flat, related_name='complaints', on_delete=models.CASCADE, verbose_name='Квартира')
    complaint_text = models.TextField(verbose_name='Текст жалобы')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Жалоба от {self.user.username} на {self.flat}"
