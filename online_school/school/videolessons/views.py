from django.contrib import messages
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import MeetingForm
from django_zoom_meetings import ZoomMeetings
from dotenv import load_dotenv
import os

load_dotenv()


class CreateMeetingView(FormView):
    template_name = 'videolessons/meeting-create.html'
    form_class = MeetingForm
    success_url = reverse_lazy('index')
    permission_classes = [AllowAny]

    def get_zoom_API(self) -> ZoomMeetings:
        """Initialize the ZoomMeetings object with environment variables."""
        return ZoomMeetings(
            os.getenv('VERIFICATION_TOKEN'),
            os.getenv('SECRET_TOKEN'),
            os.getenv('E_MAIL')
        )

    def form_valid(self, form):
        data = form.cleaned_data
        # Create a meeting via the Zoom API
        try:
            zoom = self.get_zoom_API()
            # Create the meeting, adjusting parameters based on API requirements
            create_meeting = zoom.CreateMeeting(
                date=data['date'],
                topic=data['topic'],
                meeting_duration=data['duration'],
                meeting_password=data['password'],
            )
            # Check if the meeting was created successfully
            if create_meeting:
                # Add success message
                messages.success(self.request, "Conference successfully created!")
                return super().form_valid(form)
            else:
                form.add_error(None, "Failed to create the meeting.")
                return self.form_invalid(form)
        except Exception as e:
            # Log the error and return the form error
            form.add_error(None, f"Error creating meeting: {str(e)}")
            return self.form_invalid(form)


class GetMeetingView(APIView):
    """
    View for retrieving Zoom meeting information.
    """

    def get(self, request, meeting_id):
        try:
            # Initialize the ZoomMeetings object with environment variables
            zoom = ZoomMeetings(
                os.getenv('VERIFICATION_TOKEN'),
                os.getenv('SECRET_TOKEN'),
                os.getenv('E_MAIL')
            )
            # Retrieve meeting information by ID
            response = zoom.get_meeting(meeting_id)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
