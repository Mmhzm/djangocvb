from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import book
from .serializers import serbook
# Create your views here.

class listbook(ListAPIView):
    def get(self,request):
        if request.user.is_authenticated:
            queryset=book.objects.all()
            serializer_class=serbook
            return Response({'message':'you are loggin.'})
        else:
            return Response({'message':'you are not loggin.'})
    

