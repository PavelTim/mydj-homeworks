from django.contrib import admin

from .models import Student, Teacher #, Lesson

class ScheduleInline(admin.TabularInline):
    model = Student.teachers.through
    extra = 3

# class LessonInline(admin.TabularInline):
#     model = Lesson
#     extra = 3

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name', 'group']
    inlines = [ScheduleInline, ]                 # ScheduleInline,
    include = ['teachers']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subject']
    inlines = [ScheduleInline, ]
