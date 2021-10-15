from django.contrib import admin

# Register your models here.
from .models import posts,comments


admin.site.register(posts)
admin.site.register(comments)
