from django.db import models
from django.contrib.auth.models import User
from .transaction_category import TransactionCategory

class Transaction(models.Model):
    TYPE_CHOICES = [
        ('ingreso', 'Ingreso'),
        ('gasto', 'Gasto'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(TransactionCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    tag = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.category.name} - {self.amount}'
