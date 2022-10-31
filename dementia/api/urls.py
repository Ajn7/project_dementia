from django.urls import path
from dementia.api.views import (SymptomList, symptom_Create, symptom_details, symptom_list_all)

urlpatterns = [
    
    path('list/',symptom_list_all.as_view(),name='symptom_list_all'),
     path('add/',symptom_Create.as_view(),name='symptom_create'),
    path('<int:pk>',symptom_details.as_view(),name='symptom_details'),
    path('user/<int:pk>/',SymptomList.as_view(),name='symptom_list'),
    
   
]
