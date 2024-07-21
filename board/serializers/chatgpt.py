from rest_framework import serializers

class ChatMessageSerializer(serializers.Serializer):
    """
    Serializer for chat messages in a chat application.

    Attributes:
        user_message (str): The message sent by the user in the chat.
    """
    user_message = serializers.CharField(
        help_text="The message sent by the user"
    )

    def validate_user_message(self, value):
        """
        Validate the user_message field.

        Args:
            value (str): The message text to be validated.

        Returns:
            str: The validated message text.

        Raises:
            serializers.ValidationError: If the message is empty or invalid.
        """
        if not value.strip():
            raise serializers.ValidationError("Message cannot be empty.")
        return value
