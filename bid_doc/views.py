from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import biddoc
from .serializers import biddocserializers

# Create your views here.
class itemlist (APIView):
    def get(self,request,format=None):
        item = biddoc.objects.all()[0:4]
        serializer = biddoc(item,many=True)
        return Response(serializer.data)
        
