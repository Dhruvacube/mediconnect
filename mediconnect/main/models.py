from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from datetime import timedelta
from django.utils.translation import gettext_lazy as _
from filer.fields.file import FilerFileField
from filer.fields.image import FilerImageField
from django.conf import settings


# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = FilerImageField(null=True, blank=True, related_name="doctor_image", on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    monday = models.BooleanField(default=True)
    availability_monday_start_time = models.TimeField(default=now)
    availability_monday_end_time = models.TimeField(default=now()+timedelta(hours=4))
    tuesday = models.BooleanField(default=True)
    availability_tuesday_start_time = models.TimeField(default=now)
    availability_tuesday_end_time = models.TimeField(default=now()+timedelta(hours=4))
    wednesday = models.BooleanField(default=True)
    availability_wednesday_start_time = models.TimeField(default=now)
    availability_wednesday_end_time = models.TimeField(default=now()+timedelta(hours=4))
    
    class Meta:
        verbose_name = _("Doctor")
        verbose_name_plural = _("Doctors")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("Doctor_detail", kwargs={"pk": self.pk})


class Patient(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    symptoms = models.JSONField(default=dict)
    health_data = models.JSONField(default=dict)
    extra_data = models.JSONField(default=dict)
    
    appointment_date = models.DateField(default=now)
    appointment_duration = models.DurationField(default=timedelta(hours=1))
    meeting_link = models.URLField(default="https://meet.google.com")
    
    files = FilerFileField(null=True, blank=True, related_name="extra_files", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _("Patient")
        verbose_name_plural = _("Patients")

    def __str__(self):
        return self.user + " " + str(self.appointment_date)

    def get_absolute_url(self):
        return reverse("Patient_detail", kwargs={"pk": self.pk})


class GeneralDiagnosticQuestions(models.Model):
    question = models.CharField(max_length=100)
    class Meta:
        verbose_name = _("General Diagnostic Questions")
        verbose_name_plural = _("General Diagnostic Questions")

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("GeneralDiagnosticQuestions_detail", kwargs={"pk": self.pk})


class Feedback(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    feedback = models.JSONField(_("feedback"), default=dict)
    class Meta:
        verbose_name = _("Feedback")
        verbose_name_plural = _("Feedbacks")

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("Feedback_detail", kwargs={"pk": self.pk})




