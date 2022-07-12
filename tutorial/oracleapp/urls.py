from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test),
    path('member_list/', views.view_Member_List),
    path('member/', views.view_Member),
] 
