from django.urls import path
from users.views import (GetUserList,
                         RetriveUpdateDestroyUser,
                         LogoutUser,
                         RegisterUser,
                         LoginUserView)

urlpatterns = [
    path('user-list/', GetUserList.as_view(), name='user-list'),
    path('user/<int:pk>/', RetriveUpdateDestroyUser.as_view(), name='user-detail'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),

]
