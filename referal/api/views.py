from time import sleep

from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User, UserReferral
from .serializers import (InviteSerializer, RegisterSerializer,
                          TokenSerializer, UserSerializer)
from .tokens import make_auth_code, make_invite_code


class RegistrationView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(
            phone=serializer.validated_data['phone'])
        make_auth_code(user)
        make_invite_code(user)
        sleep(2)
        return Response({'Код для авторизаций': user.auth_code,
                         'Инвайт код': user.invite_code},
                        status=status.HTTP_200_OK)


class AuthView(generics.CreateAPIView):
    serializer_class = TokenSerializer

    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(
            User,
            phone=serializer.validated_data['phone'])
        if (serializer.validated_data['auth_code']
                != user.auth_code):
            return Response({'error': 'неверный код из смс'},
                            status=status.HTTP_400_BAD_REQUEST
                            )
        return Response(
            {'refresh': str(RefreshToken.for_user(user)),
             'access': str(RefreshToken.for_user(user).access_token),
             },
            status=status.HTTP_200_OK
        )


class UserViewSet(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.request.user.referred.all()

    def post(self, request):
        serializer = InviteSerializer(data=request.data,
                                      context={'request': request})
        serializer.is_valid(raise_exception=True)
        referrer = User.objects.get(invite_code=self.request.user.invite_code)
        referred = User.objects.get(
            invite_code=serializer.validated_data['invite_code']
            )
        referrer.invite_used = True
        referrer.save()
        UserReferral.objects.create(referrer=referrer,
                                    referred=referred)
        return Response({'success': 'пригласили'},
                        status=status.HTTP_200_OK
                        )
