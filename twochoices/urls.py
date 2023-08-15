from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]