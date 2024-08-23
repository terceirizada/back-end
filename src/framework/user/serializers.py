from rest_framework import serializers


class InputCreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class OutputCreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    id = serializers.UUIDField()
