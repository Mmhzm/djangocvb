from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import book
from .serializers import serbook


from rest_framework.views import APIView
from .permission import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly

# Create your views here.

class listbook(ListAPIView):
    def get(self,request):
        if request.user.is_authenticated:
            queryset=book.objects.all()
            serializer_class=serbook
            return Response({'message':'you are loggin.'})
        else:
            return Response({'message':'you are not loggin.'})


class Publicpostuser(APIView):
    permission_classes=[AllowAny]

    def get(self,request):
        return Response({'status':'this is get'})
    def post(self,request):
        return Response({'status':'this is post'})
    
class Privatepostuser(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        return Response({'status':'login and get'})
    def post(self,request):
        return Response({'status':'login and post'})


class AdminAdminuser(APIView):
    permission_classes=[IsAdminUser]
    def get(self,request):
        return Response({'status':'login and get'})
    def post(self,request):
        return Response({'status':'login and post'})


class Readorlogin(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    def get(self,request):
        return Response({'status':'get'})
    def post(self,request):
        return Response({'status':'post'})


