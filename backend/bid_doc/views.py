from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import biddoc
from .serializers import biddocserializers

# Create your views here.
class biddoc_list (APIView):
    def get(self,request,format=None):
<<<<<<< HEAD:backend/bid_doc/views.py
        biddoc1 = biddoc.objects.all()[0:4]
        serializer = biddoc(biddoc,many=True) 
        return Response(serializer.data)      
=======
        item = biddoc.objects.all()[0:4]
        serializer = biddoc(biddoc,many=True)
        return Response(serializer.data)
>>>>>>> 53abc2a04be4da10424be12debbdd6b83633929a:bid_doc/views.py
        
