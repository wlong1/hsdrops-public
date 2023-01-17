from django.shortcuts import render
from django.http import JsonResponse
from .models import Feature
import datetime

# Create your views here.
def index(request):
    drop = Feature.objects.latest('start_date')
    return render( request, 'index.html', {'drop': drop})

def history(request):
    drops = Feature.objects.all()
    return JsonResponse({'drops':list(drops.values())})