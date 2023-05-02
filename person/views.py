from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Person
from .serializer import PersonSerializer
# Create your views here.

class PersonList(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetail(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer