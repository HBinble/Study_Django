from django.urls import path

from . import views

urlpatterns = [
    path('sample01/', views.sample_01),
    path('index01/', views.index_01),
    path('index_css02/', views.index_02),
    path('index_css03/', views.index_03),
    path('index_css04/', views.index_04),
]
