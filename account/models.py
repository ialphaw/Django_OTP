from django.db import models
from django.core.validators import MinLengthValidator


class Driver(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    national_code = models.CharField(max_length=10,
                                     validators=[MinLengthValidator(10)],
                                     unique=True)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.user.get_full_name()


class Passenger(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.user.get_full_name()                      