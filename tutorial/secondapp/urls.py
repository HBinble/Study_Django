from django.urls import path
from . import views

urlpatterns = [
    path('oneshow2/', views.oneshow2),
    path('show2/', views.show2),
    path('oneshow/', views.oneshow),
    path('show/', views.show),
    path('insert/', views.insert),
    path('main/', views.main),
] 
