from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.GetRecommendationsView.as_view(), name="get_recommendations"),
]
