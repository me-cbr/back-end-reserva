from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import *
from .models import Customer


def register_view(request):
    register_from_data = request.session.get('register_form_data', None)
    form = CustomerRegisterForm(register_from_data)

    return render(request, 'customers/pages/register_customer.html', {
        'form': form,
        'form_action': reverse('customers:register'),
    })


def register_create(request):
    if request.method != 'POST':
        raise Http404()
    
    form = CustomerRegisterForm(request.POST)
    
    if form.is_valid():
        customer = form.save(commit=False)
        customer.set_password(form.cleaned_data['password'])
        customer.save()
        messages.success(request, 'Account created successfully')
        return redirect(reverse('customers:login'))
    else:
        return render(request, 'customers/pages/register_customer.html', {
            'form': form,
            'form_action': reverse('customers:register'),
        })

def login_view(request):
    form = LoginForm()
    return render(request, 'customers/pages/login.html', {
        'form': form,
        'form_action': reverse('customers:login_create')
    })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            email=form.cleaned_data.get('email', ''),
            password=form.cleaned_data.get('password', '')
        )

        if authenticated_user:
            messages.success(request, 'Login successful')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Invalid credentials')
    else:
        messages.error(request, 'Invalid email or password')

    return redirect(reverse('customers:dashboard'))


@login_required
def logout_view(request):
    if not request.POST:
        return redirect(reverse('customers:login'))

    if request.POST.get('email') != request.user.email:
        return redirect(reverse('customers:login'))

    logout(request)
    return redirect(reverse('customers:login'))


@login_required(login_url='customers:login', redirect_field_name='next')
def dashboard(request):
    return render(request, 'customers/pages/dashboard.html')