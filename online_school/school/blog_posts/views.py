import requests
from django.shortcuts import render, redirect
from django.views.generic import View
from datetime import datetime

PATH = 'http://192.168.0.105:9000'


class PostListView(View):
    http_method_names = ['get', 'post']
    template_name = 'online_school/index.html'

    def get(self, request, *args, **kwargs):
        api_url = f'{PATH}/api/blog/'
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
        api_url = f'{PATH}/api/blog/post/{pk}/'
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            post = response.json()
            post['id'] = pk
        except requests.exceptions.RequestException as e:
            post = None
            print(f"Error fetching data from API: {e}")

        if post:
            updated_str = post.get('updated')
            updated_date = datetime.fromisoformat(updated_str.replace('Z', '+00:00'))
            post['post_date'] = updated_date.strftime('%d %b %Y')

        context = {
            'post': post,
            'title': 'Post Detail',
        }
        return render(request, self.template_name, context)


from django.shortcuts import redirect


class PostUpdateView(View):
    template_name = 'online_school/post-update.html'

    def get(self, request, pk, *args, **kwargs):
        api_url = f'{PATH}/api/blog/update/{pk}/'
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            post = response.json()
        except requests.exceptions.RequestException as e:
            post = None
            print(f"Error fetching data from API: {e}")

        context = {
            'post': post,
            'title': 'Edit Post',
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        title = request.POST.get('title')
        body = request.POST.get('body')
        api_url = f'{PATH}/api/blog/update/{pk}/'
        data = {
            'title': title,
            'body': body,
        }

        try:
            response = requests.patch(api_url, json=data)
            response.raise_for_status()
            return redirect('post-detail', pk=pk)
        except requests.exceptions.RequestException as e:
            print(f"Error updating post: {e}")
            context = {
                'post': data,
                'title': 'Edit Post',
            }
            return redirect('post-detail', pk=pk)
