import Algorithmia
import json
from django.shortcuts import render,redirect
from apps.customers.models import Customer, Friend
from django.contrib.auth.hashers import make_password
from apps.chat.models import Channel
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404, get_object_or_404
import re

# # Create your views here.
# def retrieve_user(request):
#     if request.method == "POST":
#         User.objects.create(username=request.POST['username'],password=make_password(request.POST['password'],salt=None,hasher='default'),first_name=request.POST['firstname'],last_name=request.POST['lastname'],DoB=request.POST['dob'],email_addr=request.POST['email'],hobbies=request.POST['hobby'],fav_book=request.POST['book'])
#         return redirect('thanks')
#     message={'error':"We could not create your account! Please try again"}
#     return render(request,'matching/profile.html',message)

# def thankyou(request):
#     return render(request,"matching/thankyou.html")

def matching(request):
    customer = Customer.objects.get(user_id=request.user.pk)
    others = Customer.objects.exclude(user_id=customer.id)

    for i in range(0, customer.friends.all().count()):
        others = others.exclude(id=customer.friends.all()[i].customer_id)

    # print(others)
    # accepted_match = get_list_or_404(user.friends, customer_id=user.id)
    user_profile = [
        {
            'name' : str(customer.id),
            'age'  : customer.age(),
            'interests' : customer.hobby.split(", "),
            'fav_book' : customer.favorite_book.split(", ")
        }
    ]
    matching_list = []
    for match in others:
        profile = {
            'name' : str(match.id),
            'age'  : match.age(),
            'interests' : re.split("; | , | . | \\ | // | \n  | \s",match.hobby),
            'fav_book' : re.split("; | , | . | \\ | // | \n  | \s",match.favorite_book),
        }
        matching_list.append(profile)
    result = {
        'scoring_weights' : {
            'age':0.3,
            'gender':0.6,
            'interests':0.4,
            'fav_book':0.4,
        },
        'group1' : user_profile,
        'group2' : matching_list,
    }

    client = Algorithmia.client('simWgOx7ABiLTOAxABjYTbiRrma1')
    algo = client.algo('matching/DatingAlgorithm/0.1.3')
    algo.set_options(timeout=300) # optional
    matched = algo.pipe(result).result

    matched_id = int(matched[str(customer.id)])
    matched_customer = Customer.objects.get(id=matched_id)
    matched_user = User.objects.get(id=matched_customer.user_id)

    return render(request,'matching/matched.html', {
        'matched_user_username': mark_safe(json.dumps(matched_user.username)),
        'matched_customer_id': mark_safe(json.dumps(matched_id))
    })
def add_friend(request, matched_id):
    customer = Customer.objects.get(user_id=request.user.pk)
    matched_customer = Customer.objects.get(id=matched_id)

    friend = Friend()
    friend.customer=matched_customer
    friend.save()

    customer.friends.add(friend)
    # channel = Channel.objects.get(customer_id=customer.id)
    return redirect('add_channel', matched_id)

def add_channel(request, matched_id):
    customer = Customer.objects.get(user_id=request.user.pk)
    channels = Channel.objects.all()

    for channel in channels:
        participants = channel.participants.all()
        if participants.filter(pk=customer.id).exists() and participants.filter(pk=matched_id).exists():
            return redirect('room', channel.link)

    channel = Channel.objects.create()
    channel.save()
    channel.participants.add(customer.id, matched_id)
    return redirect('room', channel.link)
