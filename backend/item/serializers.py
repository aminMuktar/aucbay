from rest_framework import serializers
from .models import category,item


class itemSerializer(serializers.ModelSerializer):
    class Meta:
<<<<<<< HEAD:backend/item/serializers.py
        model = item
=======
        model = items
>>>>>>> 53abc2a04be4da10424be12debbdd6b83633929a:item/serializers.py
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