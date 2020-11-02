"""
The module defines urls for the site
"""

from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from snippets import views


urlpatterns = [
    path('dogs/', views.DogList.as_view()),
    path('dogs/<int:pk>/', views.DogDetail.as_view()),
    path('breeds/', views.BreedList.as_view()),
    path('breeds/<int:pk>/', views.BreedDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
