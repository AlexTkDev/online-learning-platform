from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from users.enums import Role

from .models import Tests, Grades

User = get_user_model()


class TestAdmin(admin.ModelAdmin):
    list_display = ('test_name', 'test_date', 'test_from_course')
    list_filter = ('test_date', 'test_from_course')


class GradesAdminForm(forms.ModelForm):
    class Meta:
        model = Grades
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Фильтрация студентов по роли
        self.fields['student_name'].queryset = User.objects.filter(role=Role.Student.name)


class GradesAdmin(admin.ModelAdmin):
    form = GradesAdminForm
    list_display = ('test_name', 'student_name', 'date')
    list_filter = ('student_name', 'date')


admin.site.register(Tests, TestAdmin)
admin.site.register(Grades, GradesAdmin)
