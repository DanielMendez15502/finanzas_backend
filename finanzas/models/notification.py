from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    STATUS_CHOICES = [
        ('leído', 'Leído'),
        ('no leído', 'No Leído'),
    ]
    TYPE_CHOICES = [
        ('presupuesto', 'Presupuesto'),
        ('meta', 'Meta'),
        ('transacción', 'Transacción Grande'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='no leído')

    def __str__(self):
        return f'{self.message[:20]}... - {self.status}'
