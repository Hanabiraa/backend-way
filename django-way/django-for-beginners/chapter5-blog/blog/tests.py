from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post

# Create your tests here.


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username='testuser', email='test@email.com', password='secret'
        )

        cls.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, 'A good title')
        self.assertEqual(self.post.body, 'Nice body content')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(str(self.post), 'A good title')
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_url_correct_loc_list_view(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_url_correct_loc_detail_view(self):
        resp = self.client.get('/post/1/')
        self.assertEqual(resp.status_code, 200)

    def test_post_list_view(self):
        resp = self.client.get(reverse('home'))
        
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Nice body content')
        self.assertTemplateUsed(resp, 'home.html')

    def test_post_detail_view(self):
        resp = self.client.get(reverse('post_detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'A good title')
        self.assertTemplateUsed(resp, 'post_detail.html')
        
        no_resp = self.client.get('/post/1111100/')
        self.assertEqual(no_resp.status_code, 404)