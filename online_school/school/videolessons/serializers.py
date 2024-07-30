from rest_framework import serializers


class MeetingSerializer(serializers.Serializer):
    """
    Сериализатор для данных встречи Zoom.
    """
    date = serializers.DateTimeField()  # Дата и время начала встречи
    topic = serializers.CharField(max_length=255)  # Тема встречи
    duration = serializers.IntegerField()  # Длительность встречи в минутах
    password = serializers.CharField(max_length=10, required=False,
                                     allow_blank=True)  # Пароль для встречи (необязательный)
