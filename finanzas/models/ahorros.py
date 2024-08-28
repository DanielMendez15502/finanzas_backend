from django.db import models
from django.contrib.auth.models import User

class Savings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    monto_ahorrado = models.DecimalField(max_digits=10, decimal_places=2)
    meta_de_ahorro = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    mes = models.PositiveIntegerField()
    año = models.PositiveIntegerField()

    class Meta:
        unique_together = ('user', 'mes', 'año')
        verbose_name_plural = "Ahorros Mensuales"

    def __str__(self):
        return f"Ahorro de {self.user.username} en {self.mes}/{self.año}"
