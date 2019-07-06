from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.

api_key = '15da7u0446'
url = 'https://api.railwayapi.com/v2/route/train/<train number>/apikey/' + api_key + '/'


def home(request):
    return render(request, 'home.html')


def live_status(request):
    if request.method == 'POST':
        train_number = request.POST['train_number']
        code = request.POST['code']
        date = request.POST['date']
        date = date[8:] + '-' + date[5:7]+'-'+date[0:4]
        url = 'https://api.railwayapi.com/v2/live/train/' + train_number + '/station/' + code + '/date/' + date + '/apikey/' + api_key + '/'
        response_data = requests.get(url)
        data = response_data.json()
        # print(data)
        return render(request, 'live_status.html', context=data)
    else:
        return render(request, 'live_status.html')


def pnr(request):
    if request.method == 'POST':
        pnr = request.POST['pnr']
        url = 'https://api.railwayapi.com/v2/pnr-status/pnr/' + pnr + '/apikey/' + api_key + '/'
        response_ob = requests.get(url)
        result = response_ob.json()
        return render(request, 'pnr.html', context=result)

    else:
        return render(request, 'pnr.html')


def train_routes(request):
    if request.method == 'POST':
        train_number = request.POST['number']
        complete_url = 'https://api.railwayapi.com/v2/route/train/' + train_number + '/apikey/' + api_key + '/'
        respose_ob = requests.get(complete_url)
        result = respose_ob.json()
        return render(request, 'train_route.html', context=result)
    else:
        return render(request, 'train_route.html')


def seat_avalability(request):
    if request.method == 'POST':
        train_number = request.POST['train_number']
        source = request.POST['source']
        destination = request.POST['dect']
        date = request.POST['date']
        c = request.POST['class']
        date = date[8:] + '-' + date[5:7]+'-'+date[0:4]
        url = 'https://api.railwayapi.com/v2/check-seat/train/'+ train_number +'/source/'+ source +'/dest/'+ destination +'/date/'+ date +'/pref/'+ c +'/quota/GN/apikey/'+ api_key +'/'
        response_data = requests.get(url)
        data = response_data.json()
        print(data)
        return render(request, 'seat_available.html', context=data)

    else:
        return render(request, 'seat_available.html')
