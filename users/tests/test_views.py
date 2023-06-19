from django.test import TestCase, Client

from django.urls import reverse
from django.contrib.auth.models import User

class TestViews(TestCase):
    
    def setUp(self) -> None:
        self.client = Client()
        # one default user
        self.test_user = User.objects.create(
            username='test_user',
            email='test_username@gmail.com',
        )
        self.test_user.set_password('password321')
        self.test_user.save()

    def test_signup_GET(self):
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_login_GET(self):
        response = self.client.get(reverse("users:login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/login.html")

    def test_logout_GET_redirect(self):
        response = self.client.get(reverse("users:logout"))
        self.assertEqual(response.status_code, 302) # must redirect to login page

    def test_profile_GET_no_login_redirect(self):
        response = self.client.get(reverse("users:profile"))
        self.assertEqual(response.status_code, 302) # must redirect to login page
    
    def test_login_POST_and_redirect(self):
        # user created at setup
        test_user = {
            'username': 'test_user',
            'password': 'password321'
        }
        response = self.client.post(reverse("users:login"), test_user)
        self.assertEqual(response.status_code, 302) # must redirect to index page

    def test_signup_POST(self):
        test_user2 = {
            'username': 'test_user2',
            'email': 'test_user2@gmail.com',
            'password1': 'password321',
            'password2': 'password321'
        }
        response = self.client.post(reverse("users:signup"), test_user2)
        self.assertEqual(response.status_code, 302) # must redirect to login
        self.assertEqual(User.objects.get(username="test_user2").username, 'test_user2')
        self.assertEqual(User.objects.get(username="test_user2").email, 'test_user2@gmail.com')


    def test_signup_POST_no_data(self):
        data = {}
        response = self.client.post(reverse('users:signup'), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 1) # only `test_user`` at setUp