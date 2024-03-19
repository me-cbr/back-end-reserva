from django.shortcuts import render


def home(request):
    return render(request, 'restaurant/pages/home.html')

def user(request):
    return render(request, 'restaurant/pages/user.html')

