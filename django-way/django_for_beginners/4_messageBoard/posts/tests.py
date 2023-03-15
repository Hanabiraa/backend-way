from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.post = Post.objects.create(text='This is a test!')

    def test_model_content(self):
        self.assertEqual(self.post.text, 'This is a test!')

    def test_url_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_url_location_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_right_template_name(self):
        resp = self.client.get(reverse('home'))
        self.assertTemplateUsed(resp, 'home.html')

    def test_template_content(self):
        resp = self.client.get(reverse('home'))
        self.assertContains(resp, 'This is a test!')

    def test_homepage(self):
        """
        пример объединения несколько юниттестов, т.к. общий смысл
        """
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
        self.assertContains(resp, 'This is a test!')
