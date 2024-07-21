from rest_framework import serializers
from board.models.issue import Issue

class IssueSerializer(serializers.ModelSerializer):
    """
    Serializer for Issue model, used to convert Issue instances to and from JSON format.

    This serializer includes all fields of the Issue model in the serialized output.

    Meta:
        model (Issue): The Issue model that this serializer is based on.
        fields (tuple): A tuple containing all fields of the Issue model to be included in the serialized output.
    """
    class Meta:
        model = Issue
        fields = '__all__'

    def validate_title(self, value):
        """
        Validate the 'title' field to ensure it is not empty.

        Args:
            value (str): The title of the issue to be validated.

        Returns:
            str: The validated title value.

        Raises:
            serializers.ValidationError: If the title is empty or invalid.
        """
        if not value.strip():
            raise serializers.ValidationError("Issue title cannot be empty.")
        return value

    def validate_description(self, value):
        """
        Validate the 'description' field to ensure it is not empty.

        Args:
            value (str): The description of the issue to be validated.

        Returns:
            str: The validated description value.

        Raises:
            serializers.ValidationError: If the description is empty or invalid.
        """
        if not value.strip():
            raise serializers.ValidationError("Issue description cannot be empty.")
        return value
