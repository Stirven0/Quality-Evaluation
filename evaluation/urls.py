from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('modelos/', views.modelos, name='modelos'),
    path('mccall/', views.mccall, name='mccall'),
    path('boehm/', views.boehm, name='boehm'),
    path('furps/', views.furps, name='furps'),
    path('comparacion/', views.comparacion, name='comparacion'),
    path('conclusiones/', views.conclusiones, name='conclusiones'),
]

