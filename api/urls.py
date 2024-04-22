from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.BlogPostCreateList.as_view(), name="blogpost_view_create")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
