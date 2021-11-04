from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import bidder
from .serializers import bidderSerializer

# Create your views here.
class itemlist (APIView):
    def get(self,request,format=None):
        item = bidder.objects.all()[0:4]
        serializer = bidderSerializer(bidder,many=True)
        return Response(serializer.data)