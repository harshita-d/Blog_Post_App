from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogPostCreateList.as_view(), name="blogpost_view_create")
]

