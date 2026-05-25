from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(default='none', max_length=100)
    last_name = models.CharField(default='none', max_length=100, null=True, blank=True)
    ids=models.IntegerField(unique=True)
    profile_pic=models.CharField(max_length=200, null=True, blank=True)
    balance=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return self.username or f"User {self.ids}"