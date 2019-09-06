from django.contrib import admin
from .models import Board_DB,Comment_DB

# Register your models here.

admin.site.register(Board_DB)
admin.site.register(Comment_DB)