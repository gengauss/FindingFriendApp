from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Channel
from apps.customers.models import Customer
import json

# Create your views here.
def index(request):
    customer = Customer.objects.get(user_id=request.user.pk)
    channels = Channel.objects.all()
    for channel in channels:
        if customer in channel.participants.all():
            channel_link = channel.link
            break
    return redirect('room', channel_link)

@login_required
def room(request, channel_link):
    customer = Customer.objects.get(user=request.user)
    channels = Channel.objects.all()
    opponent_dict = dict()

    for channel in channels:
        if customer in channel.participants.all():
            opponent_dict[channel] = channel.participants.all().exclude(pk=customer.pk)[0]
    
    matched_customer = channels.filter(link=channel_link)[0].participants.all().exclude(pk=customer.pk)[0]
    return render(request, 'chat/room.html', {
        'channel_link_json': mark_safe(json.dumps(channel_link)),
        'user': request.user,
        'customer': customer,
        'dictionary': opponent_dict,
        'matched_customer':matched_customer,
    })

def get_last_20_messages(channel_link):
    channel = get_object_or_404(Channel, link=channel_link)
    return channel.messages.order_by('timestamp').all()[:20]


