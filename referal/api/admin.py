from django.contrib import admin
from users.models import User, UserReferral


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'phone', 'invite_used'
    )


@admin.register(UserReferral)
class UserReferralAdmin(admin.ModelAdmin):
    list_display = (
        'referrer', 'referred'
    )
