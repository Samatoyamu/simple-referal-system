from django.core.validators import RegexValidator


class PhoneValidator(RegexValidator):
    regex = '^\+?1?\d{9,15}$'
    message = 'Формат номера +99999999999'
