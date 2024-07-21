from rest_framework import serializers
from board.models.poll import Poll, PollOption

class PollOptionCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating PollOption instances.

    Attributes:
        option_text (str): The text of the poll option.
    """
    class Meta:
        model = PollOption
        fields = ['option_text']

class PollSerializer(serializers.ModelSerializer):
    """
    Serializer for Poll model, including nested PollOption instances.

    Attributes:
        options (list): A list of PollOption instances associated with the poll.
    """
    options = PollOptionCreateSerializer(many=True)

    class Meta:
        model = Poll
        fields = ['id', 'title', 'created_at', 'options']

    def create(self, validated_data):
        """
        Create a Poll instance and its associated PollOption instances.

        Args:
            validated_data (dict): A dictionary of validated data including the 'options' field.

        Returns:
            Poll: The created Poll instance with its associated PollOption instances.

        Raises:
            ValidationError: If there is an issue with creating the Poll or its PollOption instances.
        """
        options_data = validated_data.pop('options', [])
        poll = Poll.objects.create(**validated_data)
        for option_data in options_data:
            PollOption.objects.create(poll=poll, **option_data)
        return poll
