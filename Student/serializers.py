from rest_framework import serializers 
from .models import studnet
class Serstudent(serializers.ModelSerializer):
    class Meta:
        model=studnet
        fields='__all__'
        