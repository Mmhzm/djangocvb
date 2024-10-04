from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import studnet
from .serializers import Serstudent
# Create your views here.
class showallstudent(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            return Response({'message':'your method is get and you are login.'})
        else:
            return Response({'message':'your metohd is get and you are not login.'})
    def post(self,request):
        if request.user.is_authenticated:
            return Response({'message':'your method is post and you are login.'})
        else:
            return Response({'message':'your method is post and your are not login.'})
        
