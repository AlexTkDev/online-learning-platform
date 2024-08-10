import requests
from django.shortcuts import render
from django.views.generic import View
from datetime import datetime


class PostListView(View):
    http_method_names = ['get', 'post']
    template_name = 'online_school/index.html'

    def get(self, request, *args, **kwargs):
        api_url = 'http://192.168.0.102:9000/api/blog/'
        try:
            # Получаю посты из api_url
            response = requests.get(api_url)
            response.raise_for_status()  # Генерируем исключение для HTTP ошибок
            posts = response.json()
        except requests.exceptions.RequestException as e:
            posts = []
            print(f"Error fetching data from API: {e}")

        # Обработка даты
        for post in posts:
            updated_str = post.get('updated')
            updated_date = datetime.fromisoformat(updated_str.replace('Z', '+00:00'))
            post['post_date'] = updated_date.strftime('%d %b %Y')

        context = {
            'post_list': posts,
            'title': 'Blog Posts',
        }
        return render(request, self.template_name, context)


class PostDetailView(View):
    template_name = 'online_school/post-detail.html'

    def get(self, request, pk, *args, **kwargs):
        api_url = f'http://192.168.0.102:9000/api/blog/post/{pk}/'
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            post = response.json()
        except requests.exceptions.RequestException as e:
            post = None
            print(f"Error fetching data from API: {e}")

        if post:
            updated_str = post.get('updated')
            updated_date = datetime.fromisoformat(updated_str.replace('Z', '+00:00'))
            post['post_date'] = updated_date.strftime('%d %b %Y')

        context = {
            'post': post,
            'title': post['title'] if post else 'Post Detail',
        }
        return render(request, self.template_name, context)
