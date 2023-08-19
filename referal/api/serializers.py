from rest_framework import serializers
from users.models import User, UserReferral


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('phone', 'username')


class TokenSerializer(serializers.Serializer):
    phone = serializers.CharField()
    auth_code = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    referrer = serializers.SlugRelatedField(
        slug_field='phone',
        queryset=User.objects.all()
    )

    class Meta:
        model = UserReferral
        fields = ('referrer',)


class InviteSerializer(serializers.Serializer):
    invite_code = serializers.CharField()

    def validate(self, attrs):
        if not User.objects.filter(invite_code=attrs['invite_code']).exists():
            raise serializers.ValidationError(
                "Такого инвайт кода нет"
            )
        if (User.objects.get(phone=self.context['request'].user.phone)
                .invite_used is True):
            raise serializers.ValidationError(
                "Вы уже пригласили"
            )
        if self.context['request'].user.invite_code == attrs['invite_code']:
            raise serializers.ValidationError(
                "это ваш инвайт код"
            )
        return attrs
