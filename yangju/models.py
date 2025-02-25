from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="이름")
    phone_number = models.CharField(max_length=15, verbose_name="전화번호")

    class Meta:
        verbose_name = "양주고객"