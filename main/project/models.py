from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web'),
        ('frontend', 'Frontend'),
        ('ai', 'AI & ML'),
        ('mobile', 'Mobile'),
    ]

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='web'  # ✅ Correct placement
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    github_url = models.URLField()

    def __str__(self):
        return self.title
