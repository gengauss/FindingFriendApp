# from django.db import models
# from datetime import datetime
# # from auth.models import

# Create your models here.
# # Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length = 50)
#     password= models.CharField(max_length=50)
#     GENDER_CHOICES = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#     )
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default="None")
#     last_name = models.CharField(max_length=30)
#     first_name = models.CharField(max_length=30)
#     email_addr = models.CharField(max_length = 50)
#     DoB = models.DateField(null=False, blank=False)
#     hobbies= models.CharField(max_length=200)
#     fav_book=models.CharField(max_length=100)
#     def age(self):
#         return int((datetime.now().date() - self.DoB).days / 365.25)
