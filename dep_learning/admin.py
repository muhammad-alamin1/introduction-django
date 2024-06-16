from django.contrib import admin
from .models import DeepLearning

# Register your models here.
class DeepLearningAdmin(admin.ModelAdmin):
    list_display = ("id", "algorithm", "type", "upload_file", "uploaded_image")
    list_filter = ("id", "algorithm", "type")
    

admin.site.register(DeepLearning, DeepLearningAdmin)