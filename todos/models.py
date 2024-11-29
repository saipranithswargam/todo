from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='pending'  
    )
    def __str__(self):
        return f"{self.title} - {self.status}"
