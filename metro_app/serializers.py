from rest_framework import serializers


class StationsSerializer(serializers.Serializer):
    stations = serializers.JSONField()
