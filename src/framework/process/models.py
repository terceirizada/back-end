import uuid

from django.db import models

from src.framework.user.models import User


class Process(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    responsavel = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    candidato = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
