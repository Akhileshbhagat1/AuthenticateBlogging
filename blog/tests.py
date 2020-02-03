from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from blog.models import BlogPost

# Create your tests here.


class BlogpostViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='textuser',
            email='textuser@example',
            password='foobar'
        )

        BlogPost.objects.create(title='test post 1', user=self.user, body='this is the test post')
        BlogPost.objects.create(title='test post 2', user=self.user, body='this is the another test post')

        self.client = Client()
        self.url = reverse('posts')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        data = response.context_data['posts']
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0], {
            'id': 1,
            'title': 'test post 1',
            'author': self.user.username,
        })
        self.assertEqual(data[1], {
            'id': 2,
            'title': 'test post 2',
            'author': self.user.username,
        })






