from django.urls import path
from . import views

urlpatterns = [
    path("animals/", views.AnimalCreateListView.as_view()),
    path("animals/<int:animal_id>/", views.AnimalListOneUpdateDeleteView.as_view()),
]