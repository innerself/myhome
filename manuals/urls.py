from django.urls import path

from . import views

app_name = 'manuals'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home-index'),
    path('dacha/', views.dacha, name='dacha-index'),
    path('pc/', views.pc, name='pc-index'),
]
