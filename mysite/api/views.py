from rest_framework import generics
from .models import BlogPostModel
from .serializers import BlogPostSerializer

class BlogPostCreateList(generics.ListCreateAPIView):
    queryset=BlogPostModel
    serializer_class=BlogPostSerializer