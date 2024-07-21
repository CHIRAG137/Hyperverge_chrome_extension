from rest_framework import serializers
from board.models.board import Notice

class NoticeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Notice model.

    This serializer converts Notice model instances into JSON format and vice versa,
    enabling easy serialization and deserialization of Notice data.

    Meta:
        model (Notice): The model class to be serialized.
        fields (list): The list of model fields to include in the serialized output.
    """

    class Meta:
        model = Notice
        fields = ['id', 'title', 'message', 'created_at']

# Example usage:
# notice = Notice.objects.get(id=1)
# serializer = NoticeSerializer(notice)
# print(serializer.data)  # Output: {'id': 1, 'title': 'Meeting Update', 'message': 'The meeting is rescheduled to 3 PM.', 'created_at': '2023-07-21T12:00:00Z'}
