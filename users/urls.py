from django.urls import path
from .views import UserSignupView, UserLoginView, UserLogoutView, ProfileView


app_name = "users"
urlpatterns = [
    path('signup/', UserSignupView.as_view(), name="signup"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name="logout"),
    path('profile/', ProfileView.as_view(), name="profile"),
]