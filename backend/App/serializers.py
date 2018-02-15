from rest_framework import serializers
from .models import AppMessage

class AppMessageSerializers(serializers.ModelSerializer):
    class Meta:
        Model=AppMessage
        fields=('id' 'text' 'create_date' 'read')
