from django.shortcuts import render
from .models import Blog,Likes
from .serializers import ArticleSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.views import APIView
from rest_framework .response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

# Create your views here.

class Bloglist(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        blog = Blog.objects.all()
        serializer = ArticleSerializer(blog,many=True)
        return Response(
            serializer.data
        )
    def post(self,request):
            
            data = {
                'auth_name':request.user.id,
                'title':request.data.get('title'),
                'content':request.data.get('content'),

            }
            serializer = ArticleSerializer(data=data)
            if serializer.is_valid():
                serializer.save(

                )
                return Response(
                    {
                    'message':"Article created succesfuly"
                    }
                )
            return Response(
                serializer.errors
            )
    
class GetBlog(APIView):
     permission_classes = [IsAuthenticated]
     
     def get(self,request,id):
          blog = Blog.objects.get(id=id)
          serializer = ArticleSerializer(blog)
          return Response(
               serializer.data
          )
     def put(self,request,id):
        blog = Blog.objects.get(id=id)
        if request.user.id == blog.auth_name.id:
            data = {
                'auth_name':request.user.id,
                'title':request.data.get('title'),
                'content':request.data.get('content'),
                'likes':blog.likes
            }
            serializer = ArticleSerializer(blog,data=data)
            if serializer.is_valid():
               serializer.save()
               return Response(
                {
                    'message':'Blog updated successfully'
                }
            )
        return Response(
            {
               'message':'Only author can edit data' 
            }
        )
     
     def delete(self,request,id):
        blog = Blog.objects.get(id=id)
        if request.user.id == blog.auth_name.id:
            blog.delete()
            return Response(
                {
                'message':"Blog deleted successfully"
                }
            )
        return Response(
            {
               'message':"only author can delete data" 
            }
        )
     
class LikesApi(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,id):
        blog = Blog.objects.get(id=id)
        blog_like = blog.like.all().values_list('user',flat=True)
        if request.user.id in blog_like:
            blog.likes -=1
            blog.like.filter(user=request.user).delete()
        else:
             blog.likes +=1
             like_model=Likes(user=request.user,post=blog)
             like_model.save()
        blog.save()
        serializer = ArticleSerializer(blog)
        return Response(
            serializer.data,status=status.HTTP_200_OK  
        )


             
        
        
          
          

