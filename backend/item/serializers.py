from rest_framework import serializers
from .models import category,item


class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = (     
            'name',      
            "item_id",
            "item_name",
            "item_price",
            "item_img",
            "item_description",
            "item_location",
            "item_remaining_time",
            "ispection_start",
            "ispection_end", 
            "min_increment",
            "attribute",
    #New col
            "thumbnail",
            "item_date_added", 
        )