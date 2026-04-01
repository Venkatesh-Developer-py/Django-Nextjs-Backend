from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Serialname
from .models import Employedetails

class Viewname(viewsets.ModelViewSet):
    queryset = Employedetails.objects.all()
    serializer_class = Serialname

# Create your views here.