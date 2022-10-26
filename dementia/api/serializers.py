
from rest_framework import serializers
from dementia.models import symptoms

class SymptomSerlizer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField()
    description=serializers.CharField(style={'base_template':'textarea.html'})
    details=serializers.CharField(style={'base_template':'textarea.html'})
    
    
    
    def create(self,validated_data):
        return symptoms.objects.create(**validated_data)
    
    