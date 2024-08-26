from rest_framework import serializers


class InputAuthUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class JWTSerializer(serializers.Serializer):
    token = serializers.CharField()
    exp = serializers.IntegerField()
