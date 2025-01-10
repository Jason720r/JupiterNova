from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from Toolapi.models import Rarity

class RarityView(ViewSet):

    def retrieve(self, request, pk):
        rarity = Rarity.objects.get(pk=pk)
        serializer = RaritySerializer(rarity)
        return Response(serializer.data)
    
    def list(self, request):
        rarity = Rarity.objects.get(user=request.user)
        serializer = RaritySerializer(rarity)
        return Response(serializer.data)

class RaritySerializer(serializers.ModelSerializer):

    class Meta:
        model = Rarity
        fields = ('id', 'type')