from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.test),
    path('cart_list/', views.view_Cart_List),
    path('cart/', views.view_Cart),
    path('cart_insert/', views.view_set_Cart_Insert),
    path('testdict/', views.testDict),
    path('cart_list_dict/', views.view_Cart_List_dict),
] 
