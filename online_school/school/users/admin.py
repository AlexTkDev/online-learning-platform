from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from courses.models import Course

User = get_user_model()


class UserCourseInline(admin.StackedInline):
    model = Course
    extra = 0
    can_delete = True


class UserAdmin(BaseUserAdmin):
    inlines = (UserCourseInline,)


admin.site.register(User, UserAdmin)
