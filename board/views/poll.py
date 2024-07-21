from rest_framework import generics
from board.models.poll import Poll
from board.serializers.poll import PollSerializer

class PollListCreateAPIView(generics.ListCreateAPIView):
    """
    A view to list all Poll instances and create new Poll instances.

    This view uses the `ListCreateAPIView` generic class from Django REST framework to
    provide functionality for listing all polls and creating new ones.

    Attributes:
        queryset (QuerySet): The queryset of Poll instances to be listed or created.
        serializer_class (Serializer): The serializer class used to validate and serialize the data.
    """
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class PollDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    A view to retrieve, update, or delete a specific Poll instance.

    This view uses the `RetrieveUpdateDestroyAPIView` generic class from Django REST framework to
    provide functionality for retrieving, updating, or deleting a specific poll by its ID.

    Attributes:
        queryset (QuerySet): The queryset of Poll instances to be retrieved, updated, or deleted.
        serializer_class (Serializer): The serializer class used to validate and serialize the data.
    """
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
