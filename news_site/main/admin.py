from django.contrib import admin
from .models import Paper

# Register your models here.
class PaperAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "description", "content", "date")
    prepopulated_fields = {"slug": ("title")}


# Registering a model here makes it appear in the admin panel
admin.site.register(Paper)