from django.urls import path
from . import views

urlpatterns = [
    path('',views.getTimeAnalytics, name='time analytics'),
    path('time/upload/',views.uploadTimeData, name='upload timedata'),
    path('money/upload/', views.uploadAmountData, name='upload amountdata'),
    path('allData/<str:property>/<str:timeFilter>/',views.getAllData, name='get all data')
]