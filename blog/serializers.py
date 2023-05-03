from rest_framework import serializers
from rest_framework .serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Blog,Likes
class ArticleSerializer(ModelSerializer):
    
    class Meta:
        auth_user = serializers.ReadOnlyField(source='auth_user.username')
        model = Blog
        fields = '__all__'
        # exclude = ['auth_name']

    class LikeSerializer(ModelSerializer):
        class Meta:
            model = Likes
            fields = '__all__'