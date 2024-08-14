from django.urls import path
from .views import CreateMeetingView, GetMeetingView

urlpatterns = [
    # Маршрут для создания встречи
    path('create/', CreateMeetingView.as_view(), name='create-meeting'),
    # Маршрут для получения информации о встрече
    path('meeting/<str:meeting_id>/', GetMeetingView.as_view(), name='get-meeting'),

]
