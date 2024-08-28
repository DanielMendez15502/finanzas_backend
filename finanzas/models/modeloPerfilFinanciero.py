from django.db import models
from django.contrib.auth.models import User

class FinancialProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nivel_de_riesgo = models.CharField(max_length=50)
    prioridad_financiera = models.CharField(max_length=100)

    def __str__(self):
        return f"Perfil Financiero de {self.user.username}"
