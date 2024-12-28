from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from Toolapi.models import Character


class CharacterView(ViewSet):

    def retrieve(self, requesr, pk):
        character = Character.objects.get(pk=pk)