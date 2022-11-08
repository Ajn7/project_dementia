from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from user_app import models #importing token signals
from user_app.api.serializers import RegistrationSerializer

@api_view(['post'])
def logout_view(request):
    
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    
    
@api_view(['POST'])
def registration_view(request):
    
    if request.method == 'POST':
        serializer=RegistrationSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            #return Response(account) only contains email and username
            data['response'] = "Registration successfull"
            data['username'] = account.username
            data['email'] = account.email
            
            token = Token.objects.get(user=account).key
            data['token'] = token
           
        else:
            data=serializer.errors 
             
        return Response(data)  

@api_view(['POST'])
def deleteaccount_view(request):
    #permission_classes = [permissions.IsAuthenticated]
    if request.method == 'POST':
        username=request.POST["username"]
        password=request.POST["password"]
        #user =authenticate(username=username, password=password)
        try:
            user=User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"response":"User does not exist."})
        # if  user is None: not working 
        #     return Response({"response":"User does not exist."}) 
        if not user.check_password(password):
            return Response({"response":"incorrect Password"})
        
        user.delete()
        return Response({"result":"user deleted successfully"}) 
       
    
        
                 
    