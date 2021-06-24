from .views import search, info
from django.urls import path

urlpatterns = [
    # path('', info),
    path('search/', search),
    path('info/', info),
    
]