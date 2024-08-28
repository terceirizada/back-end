# Create your views here.
from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from src.core.process.application.service.list_process import ListProcess
from src.core.utils.security.jwt import decode_jwt
from src.framework.process.models import Process as ProcessModel
from src.framework.process.repository import DjangoORMProcessRepository
from src.framework.process.serializers import ListProcessOutput
from src.framework.user.models import User as UserModel


class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        token = request.headers.get("Authorization")
        token = token.split(" ")[1] if token else None
        if not token:
            raise AuthenticationFailed("No token provided", code=401)
        try:
            decode = decode_jwt(token)
            email = decode.get("email")
            if not UserModel.objects.filter(email=email).exists():
                raise AuthenticationFailed("User not found", code=401)
            return True
        except Exception:
            raise AuthenticationFailed("User not found", code=401)


class ProcessViewSet(ViewSet):
    permission_classes = [IsAuthenticated]  # noqa

    def list(self, request: Request) -> Response:
        service = ListProcess(repository=DjangoORMProcessRepository(ProcessModel))

        processes = service.execute()

        response = ListProcessOutput(instance=processes)

        return Response(data=response.data, status=200)
