from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth
from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer
from users.forms import UserRegistrationForm, UserLoginForm


class GetUserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetriveUpdateDestroyUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# User registrations
class RegisterUser(View):
    def get(self, request):
        form = UserRegistrationForm()
        context = {'form': form, 'title': 'Register'}
        return render(request, 'users/create-user.html', context)

    def post(self, request):
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            # Сначала создаем объект, но не сохраняем его в базе данных
            user = form.save(commit=False)
            # Проверяем роль пользователя
            if user.role == 'Teacher':
                # Присваиваем статус персонала
                user.is_staff = True
                # Сохраняем объект в базе данных
            user.save()
            return redirect('index')

        context = {'form': form, 'title': 'Register', 'errors': form.errors}
        return render(request, 'users/create-user.html', context)


# User login
class LoginUserView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {'form': form, 'title': 'Login'}
        return render(request, 'users/login.html', context)

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('index')
            context = {'form': form, 'title': 'Login', 'errors': form.errors}
            return render(request, 'users/login.html', context)


# Logout
class LogoutUser(View):
    def get(self, request):
        auth.logout(request)
        return redirect('index')
