from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import items
from .serializers import itemSerializer

# Create your views here.
class itemlist (APIView):
    def get(self,request,format=None):
        item = items.objects.all()[0:4]
        serializer = itemSerializer(item,many=True)
        return Response(serializer.data)
        
