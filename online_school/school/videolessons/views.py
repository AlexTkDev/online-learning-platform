from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_zoom_meetings import ZoomMeetings
from .serializers import MeetingSerializer
import os


class CreateMeetingView(APIView):
    """
    Представление для создания встречи Zoom.
    """

    def post(self, request):
        # Создаем экземпляр сериализатора с данными из запроса
        serializer = MeetingSerializer(data=request.data)

        # Проверяем валидность данных
        if serializer.is_valid():
            # Инициализируем объект ZoomMeetings с параметрами из переменных окружения
            zoom = ZoomMeetings(
                os.getenv('VERIFICATION_TOKEN'),
                os.getenv('SECRET_TOKEN'),
                os.getenv('E_MAIL')
            )
            data = serializer.validated_data  # Доступ к валидным данным
            # Создаем встречу через API Zoom
            response = zoom.create_meeting(
                date=data['date'].isoformat(),
                topic=data['topic'],
                duration=data['duration'],
                password=data.get('password', '')
            )
            # Возвращаем ответ с созданной встречей и статусом 201
            return Response(response, status=status.HTTP_201_CREATED)

        # Возвращаем ошибки валидации со статусом 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetMeetingView(APIView):
    """
    Представление для получения информации о встрече Zoom.
    """

    def get(self, request, meeting_id):
        # Инициализируем объект ZoomMeetings с параметрами из переменных окружения
        zoom = ZoomMeetings(
            os.getenv('VERIFICATION_TOKEN'),
            os.getenv('SECRET_TOKEN'),
            os.getenv('E_MAIL')
        )
        # Получаем информацию о встрече по ID
        response = zoom.get_meeting(meeting_id)
        # Возвращаем ответ с информацией о встрече и статусом 200
        return Response(response, status=status.HTTP_200_OK)
