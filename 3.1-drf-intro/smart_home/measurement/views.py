# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.forms import model_to_dict
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor, Measurement
from measurement.serializers import (SensorDetailSerializer, MeasurementSerializer, SensorSerializer,
                                     SensorVulgarisSer, SensorVulgarisDetailSer)


class SensorAPIView(APIView):
    ''' v0 версия API '''
    def get(self, request):
        '''4. Получить список датчиков. Выдается список с краткой информацией по датчикам: ID, название и описание.'''
        sensors = Sensor.objects.all()
        sensorserializer = SensorVulgarisSer(sensors, many=True)
        return Response(sensorserializer.data)
    def post(self, request):
        '''1.Создать датчик.Указываются название и описание датчика.'''
        sensorserializer = SensorVulgarisSer(data=request.data)
        sensorserializer.is_valid(raise_exception=True)
        if Sensor.objects.filter(name=request.data["name"]):
            return Response({'Post': 'sensor already exists'})
        sensorserializer.save()
        return Response({'Post': sensorserializer.data})

    def patch(self, request, *args, **kwargs):
        '''2. Изменить датчик. Указываются название и/или описание.'''
        pk = kwargs.get("pk", 1)
        if not pk:
            return Response({'error': "method PATCH not allowed"})
        try:
            sensor = Sensor.objects.get(pk=pk)
        except:
            return Response({'error': "object does not exists"})
        sensorserializer = SensorVulgarisSer(data=request.data, instance=sensor)
        sensorserializer.is_valid(raise_exception=True)
        sensorserializer.save()
        return Response({'patch': sensorserializer.data})

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
class SensorListCreate(ListCreateAPIView):
    '''1. Создать датчик. Указываются название и описание датчика. '''
    '''4. Получить список датчиков. Выдается список с краткой информацией по датчикам: ID, название и описание.'''
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    # serializer_class = SensorDetailSerializer
    # serializer_class = SensorVulgarisDetailSer

class SensorRetrieveUpdate(RetrieveUpdateAPIView):
    '''2. Изменить датчик. Указываются название и/или описание.'''
    '''3. Добавить измерение. Указываются ID датчика и температура.'''
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementCreate(CreateAPIView):
    '''3. Добавить измерение. Указываются ID датчика и температура. '''
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

# '''1. Создать датчик. Указываются название и описание датчика.'''
# '''2. Изменить датчик. Указываются название и/или описание.'''
# '''3. Добавить измерение. Указываются ID датчика и температура.'''
# '''4. Получить список датчиков. Выдается список с краткой информацией по датчикам: ID, название и описание.'''
