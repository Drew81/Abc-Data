from django.contrib import admin
from students.models import Student, Detail, Score, Classroom
# Register your models here.
admin.site.register(Student)
admin.site.register(Detail)
admin.site.register(Score)
admin.site.register(Classroom)