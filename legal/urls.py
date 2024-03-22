# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
    path('map/', views.map, name='map'),
    # Other URL patterns
]
