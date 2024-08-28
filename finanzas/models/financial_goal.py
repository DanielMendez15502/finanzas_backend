from django.db import models
from django.contrib.auth.models import User

class FinancialGoal(models.Model):
    STATUS_CHOICES = [
        ('en progreso', 'En Progreso'),
        ('completado', 'Completado'),
        ('fallido', 'Fallido'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    saved_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateField()
    deadline = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='en progreso')

    def __str__(self):
        return f'{self.name} - {self.status}'
