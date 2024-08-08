import requests
from django.shortcuts import render
from django.views.generic import View


class PostListView(View):
    http_method_names = ['get', 'post']
    template_name = 'online_school/index.html'

    def get(self, request, *args, **kwargs):
        api_url = 'http://localhost:9000/api/blog/'
        try:
            # Получаю посты из api_url
            response = requests.get(api_url)
            response.raise_for_status()  # Генерируем исключение для HTTP ошибок
            posts = response.json()
        except requests.exceptions.RequestException as e:
            posts = []
            print(f"Error fetching data from API: {e}")

        context = {
            'post_list': posts,
            'title': 'Blog Posts',
        }
        return render(request, self.template_name, context)
