from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date

# Create your models here.
class Customer(models.Model):
    class Meta:
        db_table = 'customers'
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    dob = models.DateField(default = "1999-01-01")
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='None')
    nationality = models.CharField(max_length=50, null=True)
    hobby = models.TextField(default=None, null=True)
    favorite_book = models.TextField(default=None, null=True)
    picture = models.ImageField(upload_to="profile_image", default='profile_image/default.png',
                                null=True, blank=True)

    # friends = models.ManyToManyField('Friend', related_name='users', blank=True)
    friends = models.ManyToManyField('Friend', related_name='users', blank=True)

    def age(self):
        return int((timezone.now().date() - self.dob).days / 365.25)
    def __str__(self):
        return f'{self.user.username} Customer'

class Friend(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.customer.user.username}'

