from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("user","age","ci")
    search_fields = ("user.username","age")

admin.site.register(User,UserAdmin)