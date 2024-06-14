from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class GetPagesTestCase(TestCase):
    def setUp(self):
        """Инициализация перед выполнением каждого теста"""

    def test_main_page(self):
        path = reverse('main:index')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'main/index.html')
        self.assertEqual(response.context['title'], 'Главная страница')

    def tearDown(self):
        """Дейсвтия после выполнения каждого теста"""
