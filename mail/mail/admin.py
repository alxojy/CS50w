from django.contrib import admin

# Register your models here.
from .models import User, Email

admin.site.register(User)
admin.site.register(Email)