from django.urls import path
from .views import (
    UserSignupView, 
    UserLoginView, 
    UserLogoutView, 
    ProfileView,
    PassResetView, 
    PassResetDoneView,
    PassResetConfirmView,
    PassResetCompleteView
)


app_name = "users"

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name="signup"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    path('profile/', ProfileView.as_view(), name="profile"),

    path('password-reset/', 
        PassResetView.as_view(), 
        name='password_reset'
    ),

    path('password-reset/done/',
        PassResetDoneView.as_view(),
        name="password_reset_done"
    ),

    path('password-reset/conform/<uidb64>/<token>/',
        PassResetConfirmView.as_view(),
        name="password_reset_confirm"
    ),

    path('password-reset/complete/',
        PassResetCompleteView.as_view(),
        name="password_reset_complete"
    ),
]