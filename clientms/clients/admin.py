from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Client, Comment, Vehicle

class ClientAdmin(admin.ModelAdmin):
    model = Client



class CommentInline(admin.TabularInline):
    model = Comment


class ClientAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle

admin.site.register(Client, ClientAdmin)
admin.site.register(Comment)
admin.site.register(Vehicle)

