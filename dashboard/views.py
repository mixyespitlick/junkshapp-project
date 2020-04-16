from django.shortcuts import render
from django.core.serializers import serialize
from . models import Junkshop
from django.http import HttpResponse

def index(request):
    return render(request, 'dashboard/index.html')

def junkshop_points(request):
    junkshops = serialize('geojson', Junkshop.objects.all())
    return HttpResponse(junkshops, content_type='json')
