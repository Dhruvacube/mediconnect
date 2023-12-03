from django.contrib import admin
from .models import *

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["user", "specialization", "monday", "tuesday", "wednesday"]
    list_per_page = 50

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ["user", "appointment_date", "appointment_duration"]
    list_per_page = 50

@admin.register(GeneralDiagnosticQuestions)
class GeneralDiagnosticQuestionsAdmin(admin.ModelAdmin):
    list_display = ["question"]
    list_per_page = 50

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ["patient", ]
    readonly_fields = ["patient", "feedback"]
