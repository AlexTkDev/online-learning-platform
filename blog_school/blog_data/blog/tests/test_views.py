from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from blog.models import Post


class PostTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_post(self):
        url = reverse('post-create')
        data = {
            'title': 'Test Title',
            'body': 'This is a test body.',
            'author': 'Test Author',
            'is_published': True
        }

        response = self.client.post(url, data, format='json')

        # Проверяю, что запрос вернул статус 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверяю, что запись была создана в базе данных
        post = Post.objects.get(title='Test Title')
        self.assertEqual(post.body, 'This is a test body.')
        self.assertEqual(post.author, 'Test Author')
        self.assertTrue(post.is_published)

    def test_create_post_without_required_fields(self):
        url = reverse('post-create')
        data = {
            'title': '',
            'body': '',
            'author': '',
            'is_published': True
        }

        response = self.client.post(url, data, format='json')

        # Проверяю, что запрос вернул статус 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_list_view(self):
        # Создаю записи в базе данных
        Post.objects.create(title='Title 1', body='Body 1', author='Author 1', is_published=True)
        Post.objects.create(title='Title 2', body='Body 2', author='Author 2', is_published=False)

        url = reverse('post-list')
        response = self.client.get(url)

        # Проверяю, что запрос вернул статус 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяю, что только опубликованные посты включены в результат
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Title 1')
        self.assertEqual(response.data[0]['author'], 'Author 1')

    def test_post_detail_view(self):
        post = Post.objects.create(title='Detail Title', body='Detail Body',
                                   author='Detail Author', is_published=True)

        url = reverse('post-detail', args=[post.id])
        response = self.client.get(url)

        # Проверяю, что запрос вернул статус 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяю, что данные поста корректны
        self.assertEqual(response.data['title'], 'Detail Title')
        self.assertEqual(response.data['author'], 'Detail Author')
