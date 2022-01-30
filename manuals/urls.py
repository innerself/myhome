from django.urls import path

from . import views


app_name = 'manuals'


urlpatterns = [
   path('', views.index, name='index'),
   path('home/', views.home, name='home-index'),
   path('home/<str:topic>/', views.home_topic, name='home-topic'),
   path('dacha/', views.dacha, name='dacha-index'),
   path('dacha/<str:topic>/', views.dacha_topic, name='dacha-topic'),
]
