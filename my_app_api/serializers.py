from rest_framework import serializers
from .models import userModel

class userModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=userModel
        fields=['id','name','email']
