from django import forms
from django.contrib import admin
from courses.models import Course
from django.contrib.auth import get_user_model
from users.enums import Role

User = get_user_model()


class CourseAdminForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Фильтрация студентов по роли
        self.fields['students'].queryset = User.objects.filter(role=Role.Student.name)


class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = ('course_name', 'teacher_name', 'start_date')
    filter_horizontal = ('students',)


admin.site.register(Course, CourseAdmin)
