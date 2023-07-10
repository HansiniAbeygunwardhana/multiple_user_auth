from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomerSerializer
from .models import Customer

# Create your views here.

class CustomerList(APIView):
    def get(self, request, format=None):
        users = Customer.objects.all()
        serializer = CustomerSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)   
        return Response(serializer.data)
        