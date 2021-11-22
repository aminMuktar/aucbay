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
            'auctionStatus',
            'bid_doc_created_at',
        )