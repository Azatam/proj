from django.test import TestCase

from rest_framework.test import APITestCase
from .models import Transaction, Category
from django.contrib.auth import get_user_model

class TransactionAPITests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.category = Category.objects.create(name='Food', user=self.user)
        self.transaction = Transaction.objects.create(
            amount=100.00, type='expense', category=self.category, user=self.user
        )

    def test_transaction_creation(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/api/transactions/', {
            'amount': 200.00, 'type': 'income', 'category': self.category.id
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Transaction.objects.count(), 2)
