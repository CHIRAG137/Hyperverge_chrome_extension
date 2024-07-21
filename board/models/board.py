from django.db import models

class Notice(models.Model):
    """
    A model representing a notice.

    Attributes:
        title (str): The title of the notice.
        message (str): The content/message of the notice.
        created_at (datetime): The date and time when the notice was created. Automatically set when the notice is created.
    """

    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the notice, which is its title.

        Returns:
            str: The title of the notice.
        """
        return self.title

# Example usage:
# notice = Notice(title="Meeting Update", message="The meeting is rescheduled to 3 PM.")
# print(notice)  # Output: Meeting Update
