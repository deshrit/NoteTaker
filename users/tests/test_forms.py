from django.test import TestCase
from users.forms import (
    SignupForm, 
    LoginForm, 
    UserUpdateForm, 
    PassResetForm,
    PassNewForm
)
from django.contrib.auth.models import User


class TestForms(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="user11", email="user11@gmail.com")
        self.user.set_password("password321")
        self.user.save()


    def test_takenoteform_valid_data(self):
        form = SignupForm(data={
            'email': 'email@email.com',
            'username': 'user',
            'password1': 'password321',
            'password2': 'password321'
        })
        self.assertTrue(form.is_valid())

    def test_takenoteform_invalid_data(self):
        form = SignupForm(data={
            'email': 'email',
            'username': 'user',
            'password1': 'password',
            'password2': 'password'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)


    def test_loginform_valid_data(self):
        form = LoginForm(data={
            'username': 'user11',
            'password': 'password321',
        })
        self.assertTrue(form.is_valid())

    
    def test_loginform_invalid_data(self):
        form = LoginForm(data={
            'username': '',
            'password': '',
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)


    def test_userupdate_valid_form(self):
        form = UserUpdateForm(data={
            'username': 'user22',
            'email': 'user11@gmail.com'
        })
        self.assertTrue(form.is_valid())

    def test_userupdate_invalid_form(self):
        form = UserUpdateForm(data={
            'username': '',
            'email': ''
        })
        self.assertFalse(form.is_valid())


    def test_passreset_valid_form(self):
        form = PassResetForm(data={
            'email': 'user11@gmail.com',
        })
        self.assertTrue(form.is_valid())

    def test_passreset_invalid_form(self):
        form = PassResetForm(data={
            'email': '',
        })
        self.assertFalse(form.is_valid())


    def test_passnewform_valid_form(self):
        form = PassNewForm(user=self.user, data={
            'new_password1': 'password789',
            'new_password2': 'password789'
        })
        self.assertTrue(form.is_valid())

    def test_passnewform_invalid_form(self):
        form = PassNewForm(user=self.user, data={
            'new_password1': '',
            'new_password2': ''
        })
        self.assertFalse(form.is_valid())