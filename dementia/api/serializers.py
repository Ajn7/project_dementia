
from rest_framework import serializers
from dementia.models import symptoms

class SymptomSerlizer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    title=serializers.CharField()
    description=serializers.CharField(style={'base_template':'textarea.html'})
    details=serializers.CharField(style={'base_template':'textarea.html'})
    created=serializers.DateTimeField(read_only=True)
    
    
    def create(self,validated_data):
        return symptoms.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance
    
    