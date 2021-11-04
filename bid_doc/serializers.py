from rest_framework import serializers
from .models import biddoc
class biddocserializers(serializers.ModelSerializer):
    class Met:
        model= biddoc
        fields = (
            'doc_id',
            'denial_of_val',
            'init_price',
            'deadline',
        )