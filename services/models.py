from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=50,)
    phone = models.CharField(max_length=50, default='', blank=True, null=True)

    mail = models.EmailField(max_length=50, default='', blank=True, null=True)
    created = models.DateTimeField()
    address = models.TextField(max_length=500, default='', blank=True, null=True)
    message = models.TextField(max_length=500, default='', blank=True, null=True)

    def __str__(self):
        return self.name
