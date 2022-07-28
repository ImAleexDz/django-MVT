from unicodedata import name
from django.urls import path
from fam.views import familiar, list_people

urlpatterns = [
    path('create-person/', familiar, name="family"),
    path('list-family/', list_people, name="list_family")
]