from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ingresos_mensuales = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gastos_mensuales = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ahorra_regularmente = models.BooleanField(default=False)
    porcentaje_ahorro = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
