from rest_framework import serializers

class DummySerializer(serializers.Serializer):
    zip = serializers.CharField()
    city = serializers.CharField()
    age = serializers.IntegerField()

    def __str__(self):
        return "Dummy Serializer object"