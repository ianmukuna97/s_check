from django.db import models


class ScannedMessage(models.Model):
    RISK_CHOICES = [
        ('safe', 'Safe'),
        ('caution', 'Caution'),
        ('suspicious', 'Suspicious'),
        ('scam', 'Scam'),
    ]

    text = models.TextField()
    score = models.IntegerField(default=0)
    risk_level = models.CharField(max_length=20, choices=RISK_CHOICES)
    is_scam = models.BooleanField(default=False)
    flags = models.JSONField(default=list)
    explanation = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'[{self.risk_level.upper()}] {self.text[:60]}...'
