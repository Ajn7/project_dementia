

from rest_framework import serializers
from login_app.models import auth_user

class UserSerlizer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    username=serializers.CharField()
    first_name=serializers.CharField()
    last_name=serializers.CharField()
    email=serializers.CharField()
    password=serializers.CharField()
    
    
    def create(self,validated_data):
        return auth_user.objects.create(**validated_data)
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name',instance.name)
    #     instance.description = validated_data.get('description',instance.description)
    #     instance.active = validated_data.get('active',instance.active)
    #     instance.save()
    #     return instance
    