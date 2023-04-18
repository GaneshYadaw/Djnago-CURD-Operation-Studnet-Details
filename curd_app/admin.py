from django.contrib import admin

from curd_app.models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'address')
    