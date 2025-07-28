from django.contrib import admin
from .models import Certificate
from django.utils.html import format_html

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview_image')

    def preview_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" style="border-radius: 5px;" />', obj.image.url)
        return "No Image"

    preview_image.short_description = "Image Preview"
