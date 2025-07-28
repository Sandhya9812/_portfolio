from django.db import models

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='certificates/', null=True, blank=True)  # ← Add this
    pdf = models.FileField(upload_to='certificates/')  # media/certificates/
    
    def __str__(self):
        return self.title
