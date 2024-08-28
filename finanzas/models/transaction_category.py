from django.db import models
from django.contrib.auth.models import User

class TransactionCategory(models.Model):
    TYPE_CHOICES = [
        ('ingreso', 'Ingreso'),
        ('gasto', 'Gasto'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return f'{self.name} ({self.type})'
