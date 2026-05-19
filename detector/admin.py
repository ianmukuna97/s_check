from django.contrib import admin
from .models import ScannedMessage


@admin.register(ScannedMessage)
class ScannedMessageAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'risk_level', 'score', 'text_preview', 'is_scam')
    list_filter = ('risk_level', 'is_scam', 'created_at')
    search_fields = ('text', 'explanation')
    readonly_fields = ('score', 'risk_level', 'is_scam', 'flags', 'explanation', 'created_at')
    
    def text_preview(self, obj):
        return obj.text[:60] + '...' if len(obj.text) > 60 else obj.text
    text_preview.short_description = 'Message'

# Username: admin
# Password: admin123
# Email: admin@example.com