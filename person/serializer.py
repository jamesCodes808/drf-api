from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'profile', 'name', 'bio', 'created_on', 'updated_on')
        model = Person