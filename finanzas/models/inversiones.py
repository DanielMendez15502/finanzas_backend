from django.db import models
from django.contrib.auth.models import User

class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_de_inversión = models.CharField(max_length=100)
    monto_invertido = models.DecimalField(max_digits=15, decimal_places=2)
    valor_actual = models.DecimalField(max_digits=15, decimal_places=2)
    riesgo = models.CharField(max_length=50)

    def __str__(self):
        return f"Inversión de {self.user.username}: {self.tipo_de_inversión}"
