from django.shortcuts import render, redirect, get_object_or_404
from utils.restaurant.factory import make_restaurant

from utils.restaurant.utils import calculate_classification
from .forms import ClassificationForm
from .models import Restaurant, Classification


def home(request):
    restaurant = Restaurant.objects.all().order_by('-id')
    return render(request, 'restaurant/pages/home.html', context={
        'restaurants': restaurant,
    })

def restaurant(request, id):
    return render(request, 'restaurant/pages/restaurant-view.html', context={
        'is_detail_page': True,
        'restaurant': get_object_or_404(Restaurant, id=id),
     })

def category(request, category_id):
    restaurant = Restaurant.objects.filter(
        category_id=category_id
    ).order_by('-id')
    return render(request, 'restaurant/pages/home.html', context={
        'restaurants': restaurant,
    })

def classification(request, id):
    return render(request, 'restaurant/partials/avaliation.html', context={
        'restaurant': get_object_or_404(Restaurant, id=id),
    })

def restaurant_classification(request):
    if request.method == 'POST':
        form = ClassificationForm(request.POST)
        if form.is_valid():
            classification = form.cleaned_data['classification']
            comment = form.cleaned_data['comment']
            Classification.objects.create(classification=classification, comment=comment, restaurant=restaurant)
            return redirect('restaurant/partials/avaliation-success.html')
        else:
            form = ClassificationForm()
    return render(request, 'restaurant/partials/avaliation.html', context={'form': form})