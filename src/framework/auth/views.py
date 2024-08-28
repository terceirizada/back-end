from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from src.core.utils.security.application.dto.jwt import InputAuthUserDto
from src.core.utils.security.application.service.auth_jwt import JWTCreator
from src.framework.auth.serializers import InputAuthUserSerializer, JWTSerializer
from src.framework.user.models import User as UserModel
from src.framework.user.repository.repository import DjangoORMUserRepository


class AuthViewSet(ViewSet):
    def create(self, request: Request) -> Response:
        serializer = InputAuthUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            repository = DjangoORMUserRepository(user_model=UserModel)
            service = JWTCreator(repository)
            response = service.execute(
                input=InputAuthUserDto(
                    email=serializer.validated_data["email"],
                    password=serializer.validated_data["password"],
                ),
            )
            output = JWTSerializer(instance=response)

            return Response(data=output.data, status=200)
        except Exception as e:
            return Response({"error": e.msg}, status=e.status_code)
