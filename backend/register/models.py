from django.contrib.auth.models import User
from django.db import models
from races.models import Race

class Register(models.Model):
    user = models.ForeignKey(User, related_name='register', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['-created_at',]

    def __str__(self):
        return self.first_name

class RegisteredRace(models.Model):
    order = models.ForeignKey(Register, related_name = 'items', on_delete = models.CASCADE)
    race = models.ForeignKey(Race, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id