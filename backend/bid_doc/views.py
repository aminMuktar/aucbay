from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import biddoc
from .serializers import biddocserializers

# Create your views here.
class biddoc_list (APIView):
    def get(self,request,format=None):
        biddoc1 = biddoc.objects.all()[0:4]   
        serializer = biddocserializers(biddoc1,many=True)
        return Response(serializer.data)                                
