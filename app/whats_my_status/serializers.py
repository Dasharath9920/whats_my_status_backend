from rest_framework.serializers import ModelSerializer
from .models import AmountSpent, TimeSpent

class AmountSerializer(ModelSerializer):
    class Meta:
        model = AmountSpent
        fields = '__all__'

class TimeSerializer(ModelSerializer):
    class Meta:
        model = TimeSpent
        fields = '__all__'