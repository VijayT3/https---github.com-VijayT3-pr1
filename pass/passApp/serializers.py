from rest_framework import serializers
from passApp.models import Pass


class PassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pass
        fields = ['id', 'fname', 'lname', 'travelpt']
