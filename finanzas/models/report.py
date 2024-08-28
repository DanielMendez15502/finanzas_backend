from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
    REPORT_TYPE_CHOICES = [
        ('transacciones', 'Transacciones'),
        ('presupuestos', 'Presupuestos'),
        ('metas', 'Metas'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)
    report_period = models.CharField(max_length=10, choices=[('diario', 'Diario'), ('mensual', 'Mensual'), ('anual', 'Anual')])

    def __str__(self):
        return f'{self.name} - {self.report_type}'
