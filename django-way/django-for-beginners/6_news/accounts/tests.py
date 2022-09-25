from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignupPageTests(TestCase):
    def test_url_exists_at_correct_loc(self):
        resp = self.client.get('/accounts/signup/')
        self.assertEqual(resp.status_code, 200)

    def test_signup_view_name(self):
        resp = self.client.get(reverse('signup'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed('registration/signup.html')

    def test_signup_form(self):
        resp = self.client.post(
            reverse('signup'),
            {
                'username': 'testuser',
                'email': 'testuser@email.com',
                'password1': 'testpass123',
                'password2': 'testpass123',
            },
        )
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, 'testuser')
        self.assertEqual(get_user_model().objects.all()[0].email, 'testuser@email.com')

