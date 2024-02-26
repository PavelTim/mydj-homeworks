from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from measurement.models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'sensor']

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class MeasurementVulgarisSer(serializers.Serializer):
    temperature = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)

class SensorVulgarisSer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField()
    def create(self, validated_data):
        return Sensor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        return instance

class SensorVulgarisDetailSer(serializers.Serializer):
    measurements = MeasurementVulgarisSer(read_only=True, many=True)
    name = serializers.CharField(max_length=50)
    description = serializers.CharField()

