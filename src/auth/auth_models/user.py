from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
import uuid

class BurnerUserManager(UserManager):
    def create_superuser(self, email, password, **extra_fields):
        print(email, password)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('birthday', '1971-01-01')
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, email, password, **extra_fields)



class BurnerUser(AbstractUser):

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True, db_index=True, blank=True)
    passport_country = models.CharField(max_length=15, default='IL')
    country_code = models.CharField(max_length=15, default='IL')
    city = models.TextField()
    street = models.TextField()
    address = models.TextField()
    birthday = models.DateField()
    primary_phone_number = PhoneNumberField(default='', blank=True)
    identification_number = models.CharField(max_length=15, null=False, blank=False)
    identification_type = models.CharField(default='tz', max_length=15, blank=False, null=False)

    objects = BurnerUserManager()

    class Meta:

        unique_together = ('identification_number', 'identification_type')


    def clean(self):
        self.username = self.email
        super().clean()
