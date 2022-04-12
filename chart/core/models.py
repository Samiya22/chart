from tabnanny import verbose
from django.db import models
from django.forms import CharField



class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'

    nomi = models.CharField(max_length=50)
    daromadi = models.IntegerField()

    def __str__(self):
        return self.nomi

class Social(models.Model):
    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Tarmoqlar'

    nomi = models.CharField(max_length=20)
    foydalanuvchisi = models.IntegerField()

    def __str__(self):
        return self.nomi


class Humans(models.Model):

    class Meta:
        verbose_name = 'Humans'
        verbose_name_plural = 'Odamlar'

    nomi = models.CharField(max_length=10)
    soni = models.IntegerField()

    def __str__(self):
        return self.nomi

class Telefonlar(models.Model):
    class Meta:
        verbose_name = 'Telefonlar'
        verbose_name_plural = 'telefonlar'

    nomi = models.CharField(max_length=10)
    narxi = models.IntegerField()

    def __str__(self):
        return self.nomi


class Country(models.Model):
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Davlatlar'

    nomi = models.CharField(max_length=10)
    raqami = models.IntegerField()

    def __str__(self):
        return self.nomi












