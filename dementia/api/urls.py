from django.urls import path
from dementia.api.views import symptom_list

urlpatterns = [
    
    path('list/',symptom_list,name='symptom_list'),
    #path('<int:pk>',movie_details,name='movie_details'),
]
