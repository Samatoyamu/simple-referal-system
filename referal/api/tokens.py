import random

from users.models import User


def make_auth_code(user):
    code = random.randint(1000, 9999)
    while User.objects.filter(auth_code=code).exists():
        code
    user.auth_code = code
    user.save()


def make_invite_code(user):
    code = random.randint(100000, 999999)
    while User.objects.filter(invite_code=code).exists():
        code
    user.invite_code = code
    user.save()
