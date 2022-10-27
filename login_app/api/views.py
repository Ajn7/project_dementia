
from rest_framework.decorators import api_view
from rest_framework.response import Response
from login_app.api.serializers import UserSerlizer
from login_app.models import auth_user

#function based view
@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
     movies=auth_user.objects.all()
     serializer=UserSerlizer(movies,many=True)
     return Response(serializer.data)
    if request.method == 'POST':
        serializer=UserSerlizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)   
# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#     if request.method == 'GET':
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerlizer(movie)
#         return Response(serializer.data)   
#     if request.method == 'PUT':
#         movie=Movie.objects.get(pk=pk)
#         serializer=MovieSerlizer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors) 
                    
#     if request.method == 'DELETE':
#         movie=Movie.objects.get(pk=pk)
#         movie.delete()
       