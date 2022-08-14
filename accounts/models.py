from django.db import models


class User(models.Model):

    COMPANY_CHOICES = (('Google', 'Google'),
                       ('Yandex', 'Yandex'))

    username = models.CharField(max_length=255)
    company = models.CharField(max_length=9, choices=COMPANY_CHOICES, default='Google')
    email = models.EmailField()
    password_1 = models.CharField(max_length=50)
    password_2 = models.CharField(max_length=50)


