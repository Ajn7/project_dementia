
from rest_framework import serializers
from dementia.models import questions

class QuestionSerializer(serializers.ModelSerializer):
    #username=serializers.IntegerField(read_only=True)
    #username=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=questions
        fields = "__all__"
        #exclude=('User',)
   