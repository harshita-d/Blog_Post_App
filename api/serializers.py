from rest_framework import serializers
from .models import BlogPostModel


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostModel
        fields = ["id", "title", "content", "published_date"]
