from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import send_email_celery
class userList(APIView):
    
    def post(self,request):
        
        email = request.data['email']
        mensaje = request.data['mensaje']

        send_email_celery.delay(email,mensaje)

        return Response({'mensaje':'email enviado'},status=status.HTTP_200_OK)


# Create your views here.
