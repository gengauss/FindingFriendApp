from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomerForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Customer
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from apps.chat.models import Contact


def index(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'not logged in'
    context = {'username': username}
    return render(request, 'Home/index.html', context)

@login_required
def dashboard(request):
    obj = Customer.objects.get(user_id=request.user.id)
    context = {'user': request.user, 'age': obj.age,
               'object': obj}
    return render(request, 'customers/dashboard.html', context)

@login_required
def edit_profile(request):
    customer = Customer.objects.filter(user_id=request.user.id).first()
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=Customer.objects.filter(user_id=request.user.id).first())
        # formset = ImageFormset(request.POST or None, request.FILES or None, instance=Customer.objects.filter(user_id=request.user.id).first())
        if form.is_valid():
            profile = form.save(commit=True)
            return redirect('dashboard')
    else:
        form = CustomerForm()
    return render(request, 'customers/edit_profile.html', {'form': form})

def register(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)

        customer = Customer()
        customer.user=user
        customer.save()

        # contact = Contact()
        # contact.user=customer
        # contact.save()

        return redirect('edit_profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
