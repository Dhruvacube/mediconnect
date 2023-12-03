from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from datetime import timedelta
from django.utils.timezone import now

# Create your models here.
class Prescription(models.Model):
    patient = models.ForeignKey("main.Patient", on_delete=models.CASCADE)
    medicines = models.JSONField(default=dict)
    doses = models.JSONField(default=dict)
    next_checkup_date = models.DateTimeField(default=now()+timedelta(days=7))
    
    class Meta:
        verbose_name = _("Prescription")
        verbose_name_plural = _("Prescriptions")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Prescription_detail", kwargs={"pk": self.pk})
