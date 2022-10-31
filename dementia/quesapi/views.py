from rest_framework.decorators import api_view
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

from dementia.permissions import QuestionUserOrAdminElseReadOnly
from dementia.models import questions
from dementia.quesapi.serializers import QuestionSerializer


#only a valid user is allowed to write questions,gets questions of particular user 
class QuestionList(generics.ListCreateAPIView):
    queryset = questions.objects.all()
    serializer_class =QuestionSerializer
    
    def get_queryset(self):
        pk=self.kwargs['pk']
        return questions.objects.filter(username=pk)
    
#questions of all users and can Create a new Question   
class QuestionListAll(generics.ListAPIView):
    queryset = questions.objects.all()
    serializer_class =QuestionSerializer 
    
class QuestionCreate(generics.CreateAPIView):
    queryset = questions.objects.all()
    serializer_class =QuestionSerializer 
    permission_classes=[IsAuthenticated]
    
    
#retrive and update particular question for review and answer purposes
class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = questions.objects.all()
    serializer_class =QuestionSerializer
    permission_classes=[QuestionUserOrAdminElseReadOnly] # or [AdminOrReadOnly]

       

    