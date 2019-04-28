from rest_framework import serializers
from my_api.models import Verbos

class VerbosSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    verb = serializers.CharField(max_length=50)
    meaning = serializers.CharField(max_length=50)
    language = serializers.CharField(max_length=50)

    def create(self, validated_data):
        """
        Create and return a new 'Verbos' instance , given validated data
        """
        return Verbos.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update a Verbos instance
        """
        instance.verb = validated_data.get('verb', instance.verb)
        instance.meaning = validated_data.get('meaning', instance.verb)
        instance.language = validated_data.get('language', instance.language)
        instance.save()
        return instance

