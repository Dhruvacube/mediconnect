from django.contrib import admin
from .models import *

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ["patient", "next_checkup_date"]
    list_per_page = 10
    readonly_fields = ["medicines", "doses"] 