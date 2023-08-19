from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import AuthView, RegistrationView, UserViewSet

auth_urls = [
    path('signup/', RegistrationView.as_view(), name='register'),
    path('token/', AuthView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserViewSet.as_view(), name='profile'),
]


urlpatterns = [
    path('v1/', include(auth_urls)),
]
