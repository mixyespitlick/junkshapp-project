from django.shortcuts import render
from django.core.serializers import serialize
from . models import Junkshop
from django.http import HttpResponse

def index(request):
    junkshops = Junkshop.objects.all()
    junkshops_count = Junkshop.objects.all().count()
    context = {'junkshops':junkshops, 'junkshops_count':junkshops_count,}
    return render(request, 'dashboard/index.html',context)

def junkshop_points(request):
    junkshops = serialize('geojson', Junkshop.objects.all())
    return HttpResponse(junkshops, content_type='json')



