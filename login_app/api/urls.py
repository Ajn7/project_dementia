from django.urls import path
from login_app.api.views import user_list

urlpatterns = [
    
    path('list/',user_list,name='movie_list'),
    #path('<int:pk>',movie_details,name='movie_details'),
]
