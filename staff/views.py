from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StaffSerializer
from .models import Staff

# Create your views here.

class StaffList(APIView):
    def get(self, request, format=None):
        users = Staff.objects.all()
        serializer = StaffSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(user.password)   
        return Response(serializer.data)
        