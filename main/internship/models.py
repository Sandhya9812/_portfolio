from django.db import models

class Internship(models.Model):
    company_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    certificate = models.ImageField(upload_to='internships/certificates/', blank=True, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.company_name} - {self.role}"
