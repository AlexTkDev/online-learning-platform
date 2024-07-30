from django.urls import path
from .views import CreateMeetingView, GetMeetingView

urlpatterns = [
    path('/create/', CreateMeetingView.as_view(), name='create-meeting'),  # Маршрут для создания встречи
    path('/meeting/<str:meeting_id>/', GetMeetingView.as_view(), name='get-meeting'),
    # Маршрут для получения информации о встрече
]
