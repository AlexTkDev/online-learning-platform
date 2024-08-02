from django.shortcuts import render
from django.views.generic import View


class PostListView(View):
    def get(self, request):
        context = {
            "title": "Blog Posts",
        }
        return render(request, "online_school/index.html", context)

