from django.db import models
from django.contrib.auth.models import User
from .transaction_category import TransactionCategory

class Budget(models.Model):
    PERIOD_CHOICES = [
        ('mensual', 'Mensual'),
        ('anual', 'Anual'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(TransactionCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    period = models.CharField(max_length=10, choices=PERIOD_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.amount}'
