from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, vehicle_choices, state_choices

from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'vehicle_choices': vehicle_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)

def carservice(request):
    return render(request, 'pages/carservice.html')

def bikeservice(request):
    return render(request, 'pages/bike.html')

def commericalservice(request):
    return render(request, 'pages/commerical_v.html')

def pcvservice(request):
    return render(request, 'pages/pcv.html')


def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }

    return render(request, 'pages/about.html', context)