from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('junkshop-points/', views.junkshop_points, name='junkshop-points'),
]