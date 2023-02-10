from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from whats_my_status.models import AmountSpent, TimeSpent
from .serializers import TimeSerializer, AmountSerializer
from datetime import date, timedelta

# Create your views here.
@api_view(['GET'])
def getTimeAnalytics(request):
    data = {
        'message': 'Welcome to Whats My Status app'
    }
    return Response(data)

@api_view(['GET'])
def getAllData(request, property, timeFilter):
    data = {}
    serializer = None
    if property == 'time':
        data = TimeSpent.objects.all()
        serializer = TimeSerializer(data, many=True)
    else:
        data = AmountSpent.objects.all()
        serializer = AmountSerializer(data, many=True)

    timeFilterMap = {
        'Today': 1,
        'Last Week': 7,
        '1 Month': 30,
        '3 Months': 90,
        '6 Months': 180,
        'Last Year': 365
    }

    arr = serializer.data
    filteredData = []

    if timeFilter == 'All Time':
        filteredData = arr
    else:
        for dt in arr:
            temp = dt['updatedOn']
            arr = temp.split('-')
            newDate = date(int(arr[0]),int(arr[1]),int(arr[2]))
            numberOfDays = date.today() - newDate
        
            if numberOfDays.days < timeFilterMap[timeFilter]:
                filteredData.append(dt)

    return Response(filteredData)

@api_view(['POST'])
def uploadTimeData(request):
    data = request.data
    serializer = {}

    if 'id' in data.keys():
        if data['property'] == 'time':
            item = TimeSpent.objects.get(id=data['id'])
            serializer = TimeSerializer(instance=item, data=data,partial = True)

            if serializer.is_valid():
                serializer.save()
            else:
                print('something went wrong')
        else:
            item = AmountSpent.objects.get(id=data['id'])
            serializer = AmountSerializer(instance=item, data=data,partial = True)

            if serializer.is_valid():
                serializer.save()
            else:
                print('something went wrong')

    else:
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

@api_view(['POST'])
def deleteData(request):
    data = request.data

    return Response({})