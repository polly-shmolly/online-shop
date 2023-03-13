from __future__ import unicode_literals

from django.test import TestCase
from ..models import Category
from django.urls import reverse

class TestCategoriesView(TestCase):
    fixtures = ["api/tests/fixtures/fixture_categories.json"]

    def test_categories_all_view(self):
        response = self.client.get(reverse('categories-all'))
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data, [
            {
                "id": 1,
                "name": "category1",
                "description": "some description"
            },

            {
                "id": 2,
                "name": "category2",
                "description": "some description"
            },

            {
                "id": 3,
                "name": "category3",
                "description": "some description"
            }
        ])


class TestProducerView(TestCase):
    fixtures = ["api/tests/fixtures/fixture_producers.json"]

    def test_producers_all_view(self):
        response = self.client.get(reverse('producers-all'))
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data, [
            {
                "id": 1,
                "name": "producer1"
            },

            {
                "id": 2,
                "name": "producer2"
            },

            {
                "id": 3,
                "name": "producer3"
            }
        ])


class TestDiscountView(TestCase):
    fixtures = ['api/tests/fixtures/fixture_discounts.json']

    def test_discounts_all_view(self):
        response = self.client.get(reverse('discounts-all'))
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data, [
            {
                "id": 1,
                "name": "discount1",
                "percent": 5,
                "expire_date": "2023-12-13T15:26:28Z"
            },
            {
                "id": 2,
                "name": "discount2",
                "percent": 5,
                "expire_date": "2023-12-13T15:26:28Z"
            },
            {
                "id": 3,
                "name": "discount3",
                "percent": 5,
                "expire_date": "2023-12-13T15:26:28Z"
            }
        ])


class TestPromocodeView(TestCase):
    fixtures = ['api/tests/fixtures/fixture_promocodes.json']

    def test_promocodes_all_view(self):
        response = self.client.get(reverse('promocodes-all'))
        self.assertIsInstance(response.data, list)
        self.assertEqual(response.data, [
            {
                "id": 1,
                "name": "promo1",
                "percent": 2,
                "expire_date": "2023-12-13T15:26:28Z",
                "is_allowed_to_sum_with_discounts": True
            },
            {
                "id": 2,
                "name": "promo2",
                "percent": 15,
                "expire_date": "2025-01-01T15:26:28Z",
                "is_allowed_to_sum_with_discounts": False
            },
            {
                "id": 3,
                "name": "promo3",
                "percent": 50,
                "expire_date": "2025-12-13T15:26:28Z",
                "is_allowed_to_sum_with_discounts": False
            }
        ])

