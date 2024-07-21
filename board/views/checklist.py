from rest_framework import generics
from board.models.checklist import Task
from board.serializers.checklist import TaskSerializer

class TaskUpdateView(generics.UpdateAPIView):
    """
    A view to handle updating a Task instance.

    This view uses the `UpdateAPIView` generic class from Django REST framework to
    provide functionality for updating an existing Task.

    Attributes:
        queryset (QuerySet): The queryset of Task instances to be updated.
        serializer_class (Serializer): The serializer class used to validate and serialize the data.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    """
    A view to handle listing and creating Task instances.

    This view uses the `ListCreateAPIView` generic class from Django REST framework to
    provide functionality for listing all Task instances and creating new ones.

    Attributes:
        queryset (QuerySet): The queryset of Task instances to be listed or created.
        serializer_class (Serializer): The serializer class used to validate and serialize the data.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
