from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from Toolapi.models import Weapons

class WeaponView(ViewSet):

    def retrieve(self, request, pk):
        weapon = Weapons.objects.get(pk=pk)
        serializer = WeaponSerializer(weapon)
        return Response(serializer.data)
    
    def list(self, request):
        weapon = Weapons.objects.get(user=request.user)
        serializer = WeaponSerializer(weapon)
        return Response(serializer.data)

class WeaponSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Weapons
        fields = ('id', 'title', 'damage', 'rarity')