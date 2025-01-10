from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from Toolapi.models import Alignment

class AlignmentView(ViewSet):

    def retrieve(self, request, pk):
        alignment = Alignment.objects.get(pk=pk)
        serializer = AlignmentSerializer(alignment)
        return Response(serializer.data)
    
    def list(self, request):
        alignment = Alignment.objects.get(user=request.user)
        serializer = AlignmentSerializer(alignment)
        return Response(serializer.data)
    
class AlignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alignment 
        fields = ('id', 'type')