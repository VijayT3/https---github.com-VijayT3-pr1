from django.shortcuts import render
from passApp.serializers import PassSerializer
from passApp.models import Pass
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def psr(request):
    if request.method == 'GET':
        ps = Pass.objects.all()
        serializer = PassSerializer(ps, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def psr_dtl(request, pk):
    try:
        p = Pass.objects.get(pk=pk)
    except Pass.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PassSerializer(p)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PassSerializer(p, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        p.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
