from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.


class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_loc(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_homepage_view(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed('home.html')
        self.assertContains(resp, 'Home')
