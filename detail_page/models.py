from django.db import models
from django.conf import settings  # Add this import to use AUTH_USER_MODEL

class Comment(models.Model):
    item_id = models.CharField(max_length=100)  # content_id를 저장할 필드
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Update this line
    nickname = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
