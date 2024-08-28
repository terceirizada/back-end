from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from src.core.user.application.dto.user_dto import InputCreateUser
from src.core.user.application.service.create_user import CreateUser
from src.framework.user.models import User as UserModel
from src.framework.user.repository.repository import DjangoORMUserRepository
from src.framework.user.serializers import (
    InputCreateUserSerializer,
    OutputCreateUserSerializer,
)


class UserViewSet(ViewSet):
    def create(self, request: Request) -> Response:
        serializer = InputCreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            repository = DjangoORMUserRepository(user_model=UserModel)
            service = CreateUser(repository)
            response = service.execute(
                input=InputCreateUser(
                    email=serializer.validated_data["email"],
                    password=serializer.validated_data["password"],
                ),
            )
            output = OutputCreateUserSerializer(instance=response)

            return Response(data=output.data, status=201)
        except Exception as e:
            return Response({"error": e.msg}, status=e.status_code)
