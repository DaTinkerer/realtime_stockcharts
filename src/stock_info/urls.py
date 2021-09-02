from .views import search, info
from django.urls import path

urlpatterns = [
    # path('', info),
    path('', search),
    path('info/', info),
    
]