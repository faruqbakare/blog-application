from turtle import title
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post
class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password = 'secret'
        )
        self.post = Post.objects.create(
            title = 'a good title',
            body = 'nicest body content',
            author = self.user
        )
    def test_string_representation(self):
        post = Post(title = 'a simple title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'a good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'nicest body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'nicest body content')
        self.assertTemplateUsed(response, 'home.html')
