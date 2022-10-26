
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dementia.api.serializers import SymptomSerlizer
from dementia.models import symptoms

@api_view(['GET', 'POST'])
def symptom_list(request):
    if request.method == 'GET':
     symptom=symptoms.objects.all()
     serializer=SymptomSerlizer(symptom,many=True)
     return Response(serializer.data)
    if request.method == 'POST':
        serializer=SymptomSerlizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)   
@api_view(['GET','PUT','DELETE'])
def symptom_details(request,pk):
    if request.method == 'GET':
        symptom=symptoms.objects.get(pk=pk)
        serializer=SymptomSerlizer(symptom)
        return Response(serializer.data)   
    if request.method == 'PUT':
        symptom=symptoms.objects.get(pk=pk)
        serializer=SymptomSerlizer(symptom,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors) 
                    
    if request.method == 'DELETE':
        symptom=symptom.objects.get(pk=pk)
        symptom.delete()
       