# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('pdf_query/', views.Pdfquery, name='Pdfquery'),
    
    # Other URL patterns
]
