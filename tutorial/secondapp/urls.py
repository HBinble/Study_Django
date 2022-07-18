from django.urls import path
from . import views

app_name = "second"

urlpatterns = [
    path('oneshow2/', views.oneshow2),
    path('show2/', views.show2),
    path('oneshow/', views.oneshow),
    path('show/', views.show),
    path('insert/', views.insert),
    path('main/', views.main),
    path('lprod_list/', views.view_Lprod_List),
    path('lprod/', views.view_Lprod),
    path('lprod_list_page/', views.view_Lprod_List_Page, name="lprod_list_page"),
    
] 
