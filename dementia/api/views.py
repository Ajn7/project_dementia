
from rest_framework.decorators import api_view
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from dementia.models import symptoms
from dementia.api.serializers import SymptomSerializer


#concrete view class v-5/18

#lists all symptoms and create symptom
class symptom_list_all(generics.ListAPIView):
    queryset = symptoms.objects.all()
    serializer_class =SymptomSerializer
    
class symptom_Create(generics.CreateAPIView):
    queryset = symptoms.objects.all()
    serializer_class =SymptomSerializer
    permission_classes=[IsAuthenticated]
    
    
#update 
class symptom_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = symptoms.objects.all()
    serializer_class =SymptomSerializer
    permission_classes=[IsAuthenticated]

#symptoms of paricular user and a valid user can add symptoms
class SymptomList(generics.ListCreateAPIView):
    queryset = symptoms.objects.all()
    serializer_class =SymptomSerializer
    
    def get_queryset(self):
        pk=self.kwargs['pk']
        return symptoms.objects.filter(username=pk) 
    
    permission_classes=[IsAuthenticated]