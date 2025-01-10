from django.contrib import admin
from django.urls import include, path
from Toolapi import views
from Toolapi.views import CharacterView, weaponview, rarityview, groupview, alignmentview
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'characters', CharacterView, 'character')
router.register(r'weapons', weaponview, 'weapon')
router.register(r'rarities', rarityview, 'rarity')
router.register(r'groups', groupview, 'group')
router.register(r'alignments', alignmentview, 'alignment')


urlpatterns = [
    path('', include(router.urls)),
]

