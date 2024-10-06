from .models import book
from rest_framework import serializers

class serbook(serializers.ModelSerializer):
    class Meta:
        model=book
        fields="__all__"