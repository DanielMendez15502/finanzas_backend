from django.db import models
from django.contrib.auth.models import User

class Debt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_de_deuda = models.CharField(max_length=100)
    monto_total = models.DecimalField(max_digits=15, decimal_places=2)
    monto_restante = models.DecimalField(max_digits=15, decimal_places=2)
    tasa_de_interés = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_de_vencimiento = models.DateField()

    def __str__(self):
        return f"Deuda de {self.user.username}: {self.tipo_de_deuda}"
