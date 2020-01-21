from django.db import models
from django.contrib.auth import get_user_model
from apps.customers.models import Customer
from datetime import datetime
import uuid
# Create your models here.

User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(Customer, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def time(self):
        return datetime.now().minute() - self.timestamp.minute()
    def __str__(self):
        return self.customer.user.username

class Channel(models.Model):
    participants = models.ManyToManyField(Customer, related_name='channel')
    messages = models.ManyToManyField(Message, blank=True)
    link = models.URLField(default=uuid.uuid4())

    def last_20_messages(self):
        return self.messages.objects.order_by('timestamp').all()[:20]

    def __str__(self):
        return "{}".format(self.pk)
