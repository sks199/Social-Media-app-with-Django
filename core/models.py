import uuid
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404

# Create your models here.
