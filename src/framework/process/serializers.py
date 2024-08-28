from rest_framework import serializers


class Responsavel(serializers.Serializer):
    id = serializers.UUIDField()
    email = serializers.EmailField()


class ProcessUnit(serializers.Serializer):
    id = serializers.UUIDField()
    responsavel = Responsavel()
    candidato = serializers.CharField()
    cargo = serializers.CharField()
    status = serializers.CharField()


class ListProcessOutput(serializers.Serializer):
    data = ProcessUnit(many=True)
