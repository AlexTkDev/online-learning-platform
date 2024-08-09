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

    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['role'].choices = [
            (tag.name, tag.value) for tag in Role
        ]
        return form


admin.site.register(User, UserAdmin)
