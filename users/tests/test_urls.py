from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import (
    UserSignupView, 
    UserLoginView,
    UserLogoutView,
    ProfileView,
)

class TestUrls(SimpleTestCase):

    def test_signup_resolve(self):
        url = reverse('users:signup')
        self.assertEqual(resolve(url).func.view_class, UserSignupView)
    
    def test_login_resolve(self):
        url = reverse('users:login')
        self.assertEqual(resolve(url).func.view_class, UserLoginView)

    def test_logout_resolve(self):
        url = reverse('users:logout')
        self.assertEqual(resolve(url).func.view_class, UserLogoutView)
    
    def test_profile_resolve(self):
        url = reverse('users:profile')
        self.assertEqual(resolve(url).func.view_class, ProfileView)