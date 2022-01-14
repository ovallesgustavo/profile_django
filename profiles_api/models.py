from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """ Manager para perfiles de Usuario """

    def create_user(self, email, name, password=None):
        """ Crear un nuevo perfil de Usuario """
        if not email:
            raise ValueError('El usuario debe tener un Email')

        email = self.normalize_email(email)
        user = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Modelo de la Base de Datos para Usuarios en el Sistema"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        ''' Obtener el Nombre Completo del Usuario '''
        return self.name

    def get_short_name(self):
        ''' Obtener el Nombre Completo del Usuario '''
        return self.name
    
    def __str__(self):
        ''' Retorna la Cadena que representa a nuestro Usuario '''
        return self.email
    
