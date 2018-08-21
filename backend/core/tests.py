import json

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class CoreModuleTests(TestCase):
    def test_logout(self):
        get_user_model().objects.create_user(phone_number='13312345678')
        self.client.force_login(get_user_model().objects.get(phone_number='13312345678'))

        response = self.client.get(reverse('api:core:logout'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['message'], 'User logged out.')

        response = self.client.get(reverse('api:core:is-authenticated'))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(json.loads(response.content)['is_authenticated'])

    def test_delete_customer(self):
        get_user_model().objects.create_user(phone_number='14412345678')
        first_user = get_user_model().objects.get(phone_number='14412345678')
        first_user_id = first_user.id
        self.client.force_login(first_user)

        response = self.client.delete(reverse('api:core:delete-user'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['message'], 'Object deleted.')

        response = self.client.post(
            reverse('api:customers:forestage:get-verification-code'),
            {'phone_number': '14412345678'}
        )
        verification_code = json.loads(response.content)['verification_code']

        response = self.client.post(
            reverse('api:customers:forestage:authenticate-customer'),
            {'phone_number': '14412345678', 'verification_code': verification_code}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(json.loads(response.content)['is_new_customer'])
        second_user_id = get_user_model().objects.get(phone_number='14412345678').id
        self.assertNotEqual(second_user_id, first_user_id)

        response = self.client.get(reverse('api:core:is-authenticated'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(json.loads(response.content)['is_authenticated'])

        response = self.client.delete(reverse('api:core:delete-user'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['message'], 'Object deleted.')

        response = self.client.post(
            reverse('api:customers:forestage:get-verification-code'),
            {'phone_number': '14412345678'}
        )
        verification_code = json.loads(response.content)['verification_code']

        response = self.client.post(
            reverse('api:customers:forestage:authenticate-customer'),
            {'phone_number': '14412345678', 'verification_code': verification_code}
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(json.loads(response.content)['is_new_customer'])
        third_user_id = get_user_model().objects.get(phone_number='14412345678').id
        self.assertNotEqual(third_user_id, second_user_id)

        response = self.client.get(reverse('api:core:is-authenticated'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(json.loads(response.content)['is_authenticated'])

        self.client.logout()
