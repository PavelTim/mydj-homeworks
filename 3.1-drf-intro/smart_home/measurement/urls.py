from django.urls import path

from measurement.views import SensorAPIView, SensorRetrieveUpdate, MeasurementCreate, SensorListCreate

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('v0/sensors/', SensorAPIView.as_view()),
    path('v0/sensors/<pk>/', SensorAPIView.as_view()),

    # 1.POST 4.GET
    path('sensors/', SensorListCreate.as_view()),
    path('sensors/<pk>/', SensorRetrieveUpdate.as_view()),
    path('measurements/', MeasurementCreate.as_view()),


]
