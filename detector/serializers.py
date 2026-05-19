from rest_framework import serializers
from .models import ScannedMessage


class MessageInputSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=5, max_length=5000)


class ScannedMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScannedMessage
        fields = '__all__'
