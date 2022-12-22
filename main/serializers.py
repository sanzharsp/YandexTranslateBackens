from rest_framework import serializers




class TranslateSerializer(serializers.Serializer):
    targetLanguageCode = serializers.CharField(max_length=10)
    sourceLanguageCode = serializers.CharField(max_length=10)
    text = serializers.CharField()