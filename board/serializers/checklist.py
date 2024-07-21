from rest_framework import serializers
from board.models.checklist import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model, used to convert Task instances to and from JSON format.

    Meta:
        model (Task): The Task model that this serializer is based on.
        fields (list): List of fields to be included in the serialized output.
    """
    class Meta:
        model = Task
        fields = ['id', 'text', 'completed']

    def validate_text(self, value):
        """
        Validate the 'text' field to ensure it is not empty.

        Args:
            value (str): The text of the task to be validated.

        Returns:
            str: The validated text value.

        Raises:
            serializers.ValidationError: If the text is empty or invalid.
        """
        if not value.strip():
            raise serializers.ValidationError("Task text cannot be empty.")
        return value
