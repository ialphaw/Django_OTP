from django.db import models


class AuthUser(models.Model):
    phone = models.CharField(max_length=11)
    auth_code = models.CharField(max_length=6)

    def __str__(self):
        return self.auth_code