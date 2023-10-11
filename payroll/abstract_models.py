from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel


class CommonInfo(TimeStampedModel):
    id = models.UUIDField(primary_key=True,db_index=True, default=uuid.uuid4, editable=False, serialize=True)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True, blank=True)
    
    class Meta:
        abstract = True

class CommonOrganization(CommonInfo):
    telephone = models.CharField(blank=True, null=True, max_length=20)
    email = models.EmailField(blank=True, null=True, max_length=200)

    class Meta:
        abstract = True

