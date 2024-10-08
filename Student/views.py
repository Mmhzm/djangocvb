from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import studnet
from .serializers import Serstudent
from rest_framework.generics import GenericAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,ListAPIView,RetrieveAPIView
# Create your views here.
class showallstudent(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            all_student=studnet.objects.all()
            ser=Serstudent(all_student,many=True)
            return Response({'message':ser.data})
        else:
            return Response({'message':'your metohd is get and you are not login.'})
    def post(self,request):
        if request.user.is_authenticated:
            ser=Serstudent(data=request.data)
            if not ser.is_valid():
                return Response({'message':'your data isnt valid.'})
            else:
                ser.save()
                return Response({'message':'your method is post and you are login.'})
        else:
            return Response({'message':'your method is post and your are not login.'})
        
class logoutToken(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            request.user.auth_token.delete()
            return Response({'message':'logout ok!'})
        else:
            return Response({'message':'not login'})
                

class liststudent(ListAPIView):
    queryset=studnet.objects.all()
    serializer_class=Serstudent

class createstudent(CreateAPIView):
    queryset=studnet.objects.all()
    serializer_class=Serstudent
class deletestudent(DestroyAPIView):
    queryset=studnet.objects.all()
    serializer_class=Serstudent
class updatestudent(UpdateAPIView):
    queryset=studnet.objects.all()
    serializer_class=Serstudent
class detailstudent(RetrieveAPIView):
    queryset=studnet.objects.all()
    serializer_class=Serstudent
    
