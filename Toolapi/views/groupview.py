from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from Toolapi.models import Group

class GroupView(ViewSet):

    def retrieve(self, request, pk):
        group = Group.objects.get(pk=pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)
    
    def list(self, request):
        group = Group.objects.get(user=request.user)
        serializer = GroupSerializer(group)
        return Response(serializer.data)
    
class GroupSerializer(serializers.ModelSerializer):

        class Meta:
            model = Group
            fields = ('id', 'Name', 'alignment')