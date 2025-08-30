from rest_framework import viewsets, permissions
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer

class ReadOnlyOrAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        # Anyone can read; write requires auth
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True
        return request.user and request.user.is_authenticated

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("name")
    serializer_class = CategorySerializer
    permission_classes = [ReadOnlyOrAuthenticated]
    filterset_fields = ["name"]
    search_fields = ["name"]
    ordering_fields = ["name","created_at"]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related("category").all()
    serializer_class = TaskSerializer
    permission_classes = [ReadOnlyOrAuthenticated]
    filterset_fields = ["is_completed", "priority", "category"]
    search_fields = ["title", "description"]
    ordering_fields = ["due_date","priority","created_at","updated_at"]
