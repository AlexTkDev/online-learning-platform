from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from courses.models import Course
from users.enums import Role

User = get_user_model()


class UserCourseInline(admin.StackedInline):
    model = Course.students.through
    extra = 0
    can_delete = True


class UserAdmin(BaseUserAdmin):
    inlines = (UserCourseInline,)
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

    readonly_fields = (
        'role', 'is_staff', 'is_superuser', 'username', 'last_login', 'date_joined')

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)

        if obj and obj.role == Role.Student.value:
            # Убираю права и группы для студентов
            fieldsets = [
                (name, {'fields': [field for field in fields['fields'] if
                                   field not in ('groups', 'user_permissions')]})
                for name, fields in fieldsets
            ]

        return fieldsets

    # Возможность изменять через админку поле "Role"
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     form.base_fields['role'].choices = [
    #         (role.value, role.value) for role in Role
    #     ]
    #     return form


admin.site.register(User, UserAdmin)
