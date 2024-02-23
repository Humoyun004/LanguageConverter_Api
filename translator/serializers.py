from rest_framework import serializers
from .models import TextTrans, FileTrans


class TextTransSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextTrans
        fields = '__all__'


class FileTransSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileTrans
        fields = '__all__'
