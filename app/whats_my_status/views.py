from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from whats_my_status.models import AmountSpent, TimeSpent
from .serializers import TimeSerializer, AmountSerializer

# Create your views here.
@api_view(['GET'])
def getTimeAnalytics(request):
    data = {}

    return Response(data)

@api_view(['POST'])
def uploadTimeData(request):
    data = request.data

    newData = TimeSpent.objects.create(
        property = data['property'],
        timeSpentOn = data['timeSpentOn'],
        time = data['time']
    )

    serializer = TimeSerializer(newData, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def uploadAmountData(request):
    data = request.data

    newData = AmountSpent.objects.create(
        property = data['property'],
        amountSpentOn = data['amountSpentOn'],
        amount = data['amount']
    )

    serializer = AmountSerializer(newData, many=False)

    return Response(serializer.data)
