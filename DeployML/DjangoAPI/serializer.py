from rest_framework import serializers
from .models import Surveyor

class SurveyorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Surveyor
        fields = '__all__'

