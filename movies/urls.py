from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("movies/", views.Movieview.as_view()),
    path("movies/<int:movie_id>/", views.MovieDetailView.as_view()),
    path("movies/<int:movie_id>/orders/", views.MovieOrderView.as_view()),
]
