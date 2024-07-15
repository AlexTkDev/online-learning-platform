from django.urls import path
from users.views import GetUserList, RetriveUpdateDestroyUser

urlpatterns = [
    path('user-list/', GetUserList.as_view(), name='user-list'),
    path('user/<int:pk>/', RetriveUpdateDestroyUser.as_view(), name='user-detail'),
]