from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name

class Task(models.Model):
    PRIORITY_CHOICES = [(1, "High"), (2, "Medium"), (3, "Low")]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES, default=3)
    category = models.ForeignKey(Category, null=True, blank=True,
                                 on_delete=models.SET_NULL, related_name="tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["is_completed", "priority", "due_date", "-created_at"]

    def __str__(self): return self.title

    @property
    def is_overdue(self):
        return bool(self.due_date and self.due_date < timezone.localdate() and not self.is_completed)

