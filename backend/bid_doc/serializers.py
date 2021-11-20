from rest_framework import serializers
from .models import biddoc
class biddocserializers(serializers.ModelSerializer):
    class Met:
        model= biddoc
        fields = (
            'denial_of_val',
            'init_price',
            'deadline',
           ' bidCount',
            'highBidder', 
<<<<<<< HEAD:backend/bid_doc/serializers.py
            'auctionStatus', 
            'bid_doc_created_at',          
=======
            'auctionStatus',
            'bid_doc_created_at',
>>>>>>> 53abc2a04be4da10424be12debbdd6b83633929a:bid_doc/serializers.py
        )