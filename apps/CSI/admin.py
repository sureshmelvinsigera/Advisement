from django.contrib import admin
from apps.CSI.models import advisor
from apps.CSI.models import student
from apps.CSI.models import office_hours

# Register your models here.
admin.site.register(office_hours)
admin.site.register(advisor)
admin.site.register(student)
