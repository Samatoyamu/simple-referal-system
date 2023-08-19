from api.validators import PhoneValidator
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField('Номер телефона',
                             max_length=15,
                             unique=True,
                             validators=(PhoneValidator(),))
    auth_code = models.CharField(max_length=4,
                                 blank=True,
                                 null=True)
    invite_code = models.CharField(max_length=6,
                                   blank=True,
                                   null=True,
                                   unique=True)
    invite_used = models.BooleanField(default=False)
    REQUIRED_FIELDS = ('phone',)

    def __str__(self) -> str:
        return str(self.phone)


class UserReferral(models.Model):
    referrer = models.ForeignKey(User,
                                 related_name="referrer",
                                 help_text='Кто приглашает',
                                 on_delete=models.CASCADE)
    referred = models.ForeignKey(User,
                                 related_name="referred",
                                 help_text='Приглашенный',
                                 on_delete=models.CASCADE)

    class Meta:
        unique_together = (('referrer', 'referred'),)
