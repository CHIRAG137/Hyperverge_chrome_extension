from django.db import models

class Issue(models.Model):
    """
    Represents an issue or ticket in the system.

    Attributes:
        title (str): The title or summary of the issue.
        description (str): A detailed description of the issue.
        created_at (datetime): The date and time when the issue was created. Automatically set when the issue is created.
    """
    title = models.CharField(max_length=255, help_text="Title or summary of the issue")
    description = models.TextField(help_text="Detailed description of the issue")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the issue was created")

    def __str__(self):
        """
        Returns a string representation of the issue.

        Returns:
            str: The title of the issue.
        """
        return self.title
