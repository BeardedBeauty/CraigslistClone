from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.home, name = "start"),
    path("search", views.search, name = "search")
]