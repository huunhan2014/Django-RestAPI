from django.contrib import admin
from .models import Schools, Classes, Students


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name_student', 'birth_date', 'sex', 'classes')
    list_filter = ['sex', 'classes']
    search_fields = ['name_student']


class StudentInline(admin.TabularInline):
    model = Students
    extra = 3


class ClassesAdmin(admin.ModelAdmin):
    list_display = ('name_class', 'grade', 'schools')
    list_filter = ['schools', 'grade']
    search_fields = ['name_class']
    inlines = [StudentInline]


class ClassesInline(admin.TabularInline):
    model = Classes
    extra = 2


class SchoolsAdmin(admin.ModelAdmin):
    list_display = ('name_school', 'grade')
    list_filter = ['grade']
    search_fields = ['name_school']
    inlines = [ClassesInline]


admin.site.register(Schools, SchoolsAdmin)
admin.site.register(Classes, ClassesAdmin)
admin.site.register(Students, StudentAdmin)
