from rest_framework import serializers
from .models import Practice

class PracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practice
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)
        