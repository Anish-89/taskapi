from rest_framework import serializers
from .models import Task, Category
from django.utils import timezone

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "created_at"]

class TaskSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field="name", queryset=Category.objects.all(), allow_null=True, required=False
    )
    is_overdue = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = ["id","title","description","is_completed","due_date",
                  "priority","category","is_overdue","created_at","updated_at"]

    def validate_due_date(self, value):
        if value and value < timezone.localdate():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value
