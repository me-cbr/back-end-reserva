import os

from django.contrib import messages
from django.db.models import Q
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from utils.restaurant.pagination import make_pagination

from utils.restaurant.utils import calculate_classification
from .forms import ClassificationForm
from .models import *

PER_PAGE = int(os.environ.get('PER_PAGE', 6))


def home(request):
    restaurant = Restaurant.objects.all().order_by('-id')

    messages.error(request, 'Error message')
    messages.success(request, 'Success message')
    messages.info(request, 'Info message')
    page, pagination = make_pagination(request, restaurant, PER_PAGE)

    return render(request, 'restaurant/pages/home.html', context={
        'restaurant': page,
        'pagination': pagination,
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

    page, pagination = make_pagination(request, restaurant, PER_PAGE)

    return render(request, 'restaurant/pages/home.html', context={
        'restaurants': page,
        'pagination': pagination,
        'title': f'{restaurant[0].category.name} - Category | '
    })

def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    restaurant = Restaurant.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term)
        )
    ).order_by('-id')

    page, pagination = make_pagination(request, restaurant, PER_PAGE)

    return render(request, 'restaurant/pages/search.html', {
        'page_title': f'Search for "{search_term}" |',
        'search_term': search_term,
        'restaurants': page,
        'pagination': pagination,
        'additional_url_query': f'&q={search_term}',
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