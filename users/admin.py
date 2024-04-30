from django.contrib import admin
from .models import CustomUser


class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name", "birth_date"]

    def birth_date(self, obj):
        return obj.date_of_birth.strftime('%b %d, %Y')

admin.site.register(CustomUser, UserAdmin)