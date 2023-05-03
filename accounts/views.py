from django.shortcuts import render
from rest_framework .views import APIView
from rest_framework .response import Response
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.

class Register(APIView):

    def post(self,request):
        name = request.data.get('name')
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not User.objects.filter(username=username):
            User.objects.create_user(
                first_name=name,
                username=username,
                email=email,
                password=password,
            )
            return Response(
                {
                'message':'account created succesfully'
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                'message':'username exist'
                },
                status=status.HTTP_400_BAD_REQUEST
        )
    
class Login(APIView):
    permission_classes = []

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username,password=password)
        if user:
            token,created = Token.objects.get_or_create(user=user)
            return Response(
                {
                'message':'Login successfull',
                'token':token.key
                }
            )
        return Response(
            {
            'message':'invalid username or password'
            }
        )
                

