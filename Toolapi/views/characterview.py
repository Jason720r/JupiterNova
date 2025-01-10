from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from Toolapi.models import Character


class CharacterView(ViewSet):

    def retrieve(self, request, pk):
        character = Character.objects.get(pk=pk)
        serializer = CharacterSerializer(character)
        return Response(serializer.data)
    
    def list(self, request):
        character = Character.objects.get(user=request.user)
        serializer = CharacterSerializer(character)
        return Response(serializer.data)
    
class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields = ('id', 'user', 'bio', 'alignment')
