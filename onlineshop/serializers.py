from rest_framework import serializers
from django.contrib.auth .models import User
from .models import product
from rest_framework_simplejwt.tokens import RefreshToken




class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only= True)
    isAdmin = serializers.SerializerMethodField(read_only= True)
    class Meta:
        model = User
        fields= ['id' , 'username' , 'email' , 'name' , 'isAdmin']
    def get_name(self , obj):
        name = obj.first_name
        if name == '':
            name= obj.email
        return name
    def get_isAdmin(self , obj):
        return obj.is_staff

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model= product
        fields='__all__'



