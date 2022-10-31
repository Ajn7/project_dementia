from django.urls import path
from dementia.quesapi.views import ( QuestionCreate, QuestionList,QuestionDetail, QuestionListAll)

urlpatterns = [
    
    path('user/<int:pk>/',QuestionList.as_view(),name='question_list'),
    path('<int:pk>/',QuestionDetail.as_view(),name='question_details'),
    path('list/',QuestionListAll.as_view(),name='question_all_list'),
    path('add/',QuestionCreate.as_view(),name='question_create'),
   
]
