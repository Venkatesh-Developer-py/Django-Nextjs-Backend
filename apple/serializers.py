from rest_framework import serializers
from .models import Employedetails

class Serialname(serializers.ModelSerializer):
    class Meta:
        model = Employedetails
        fields = '__all__'