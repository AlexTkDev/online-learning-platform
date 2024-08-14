from django import forms


class MeetingForm(forms.Form):
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    topic = forms.CharField(max_length=255)
    duration = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
