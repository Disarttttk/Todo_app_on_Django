from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .forms import UserLoginForm, UserRegistrationForm


class RegisterUserTestCase(TestCase):
    def setUp(self):
        self.data = {
            "username": 'user_1',
            "email": "user1@mail.ru",
            "password1": "12345678Aa",
            "password2": "12345678Aa"
        }

    def test_valid_form(self):
        form = UserRegistrationForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_form_registration_get(self):
        path = reverse('user:registration')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_success(self):
        user_model = get_user_model()
        path = reverse('user:registration')
        response = self.client.post(path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('main:index'))
        self.assertTrue(user_model.objects.filter(username=self.data['username']).exists())

    def test_user_registration_password_error(self):
        self.data['password2'] = '12345678A'

        path = reverse('user:registration')
        response = self.client.post(path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Введенные пароли не совпадают")

    def test_user_registration_exists_error(self):
        user_model = get_user_model()
        user_model.objects.create(username=self.data['username'])

        path = reverse('user:registration')
        response = self.client.post(path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Пользователь с таким именем уже существует")


class LoginUserTestCase(TestCase):
    def setUp(self):
        user_model = get_user_model()
        self.form_data = {'username': 'testuser', 'password': 'password123'}
        self.user = user_model.objects.create_user(username=self.form_data['username'],
                                                   password=self.form_data['password'])

    def test_valid_form(self):
        form = UserLoginForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_get(self):
        path = reverse('user:login')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_user_login_success(self):
        path = reverse('user:login')
        response = self.client.post(path, self.form_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('main:index'))

    def test_user_login_error(self):
        self.form_data['password'] = 'wrongpassword'
        path = reverse('user:login')
        response = self.client.post(path, self.form_data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Неверное имя пользователя или пароль. Попробуйте ещё раз.')

