from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import uuid  # Import UUID module to generate unique IDs

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=100, default=uuid.uuid4)  # Add session ID field
    
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'
    class Meta:
        app_label = 'chatbot'