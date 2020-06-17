from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Autor,Libro
from .serializers import autorserializers, libroserializers
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
def autor_api(request):
    if request.method == 'GET':
        data = Autor.objects.all()
        serializers = autorserializers(data,many=True) 
        return Response(serializers.data)
    elif(request.method == 'POST'):
        serializers = autorserializers(data=request.data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def libro_api(request):
    if request.method == 'GET':
        data = Libro.objects.all()
        serializers = libroserializers(data,many=True) 
        return Response(serializers.data)
   
@api_view(['GET'])
def libro_esp(request, id):
    if request.method == 'GET':
        data = Libro.objects.filter(autor_id = id)
        serializers = libroserializers(data,many=True) 
        return Response(serializers.data)


@api_view(['POST'])
def crear_libro(request):
    if request.method == 'POST':
        serializers = libroserializers(data=request.data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
   

