from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.contrib.auth .models import User
from rest_framework.response import Response
from .models import product
from .serializers import productSerializer , UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['email'] = self.user.email

        return data

   

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def index(request):
    routes = [
        '/api/products/create/',
        '/api/products/upload/',
        '/api/products/<id>/reviews/',
        '/api/products/top/',
        '/api/products/<id>/',
        '/api/products/delete/<id>/',
        '/api/products/update/<id>/',
    ]
    return Response(routes) 


@api_view(['GET'])
def getUserProfile(request):
    user = request.user
    serializer =UserSerializer(user , many =False)
    return Response(serializer.data)



@api_view(['GET'])
def getProduct(request):
    productlist= product.objects.all()
    serializer = productSerializer(productlist , many = True)
    return Response(serializer.data)

@api_view(['GET'])
def singleproduct(request , pk):
    productlist = product.objects.get(id=pk)
    serializer = productSerializer(productlist ,many = False)
    return Response(serializer.data)

    