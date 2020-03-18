from . import views
from django.urls import path, include

urlpatterns = [path("", views.home, name = "start.html"), path("new-search/", views.new_search, name = "new_search")]