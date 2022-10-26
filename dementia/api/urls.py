from django.urls import path
from dementia.api.views import symptom_details, symptom_list

urlpatterns = [
    
    path('list/',symptom_list,name='symptom_list'),
    path('<int:pk>',symptom_details,name='symptom_details'),
]
