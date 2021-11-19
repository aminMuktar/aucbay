from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import item
from .serializers import itemSerializer

# Create your views here.
class itemlist (APIView):
    def get(self,request,format=None):
        item1 = item.objects.all()[0:4]
        serializer = itemSerializer(item,many=True)
        return Response(serializer.data)
        
