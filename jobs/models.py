from django.db import models
from django.contrib.auth.models import User

class JobApplication(models.Model):
    user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    null=True,
    blank=True
)
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Rejected', 'Rejected'),
        ('Offer', 'Offer'),
    ]

    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_location = models.CharField(max_length=100, blank=True)
    applied_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company_name} - {self.job_title}"