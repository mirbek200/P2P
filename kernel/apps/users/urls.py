from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (LoginView, RegistrationView,
                    ActivationView, ChangePasswordView,
                    RestorePasswordView, RestorePasswordCompleteView,
                    MyUserDetailView)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('user_detail/<int:pk>/', MyUserDetailView.as_view(), name='register'),

    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('activation/<str:otp>/', ActivationView.as_view()),
    path('restore_password/', RestorePasswordView.as_view()),
    path('restore_complete/', RestorePasswordCompleteView.as_view()),
    path('change_password/', ChangePasswordView.as_view())
]
