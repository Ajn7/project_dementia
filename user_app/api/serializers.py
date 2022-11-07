from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    
    class Meta:
        model=User
        fields=['username','email','password','password2']
        #to set password write only password
        extra_kwargs={
            'password':{'write_only':True}
        }
    #before storing all the checking is done 
    #for that modify the save method here
    def save(self):
        
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'email already exists'})
        
        # if User.objects.filter(username=self.cleaned_data['username']).exists():
        #     raise serializers.ValidationError({'error':'username already exists'})
    
        if password!= password2:
            raise serializers.ValidationError({'error':'Password1 and Password2 must be same'})
        
        account=User(email=self.validated_data['email'],username=self._validated_data['username'])
        account.set_password(password)
        account.save()
        return account