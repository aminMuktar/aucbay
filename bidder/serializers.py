from rest_framework import serializers
from .models import bidder


class biderSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = bidder
        fields = (
          'bidder_id',
          'bidder_firstname', 
          'bidder_lastname', 
         # 'bidder_email',
          # 'bidder_password', 
           #'username',
           'USERNAME_FIELD ',
           'email'
          )

    def create(self, validated_data):
        user = super(biderSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user