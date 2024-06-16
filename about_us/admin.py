from django.contrib import admin
from .models import Member, Student

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date", "phone", "joined_date")
    
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "stu_id", "stu_name", "stu_email")

admin.site.register(Student, StudentAdmin)
admin.site.register(Member, MemberAdmin)