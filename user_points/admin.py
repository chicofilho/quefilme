from django.contrib import admin
from quefilme.user_points.models import PointMeasure

class PointMeasureAdmin(admin.ModelAdmin):
    pass
admin.site.register(PointMeasure, PointMeasureAdmin)
