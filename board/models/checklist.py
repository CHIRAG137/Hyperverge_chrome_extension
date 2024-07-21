from django.db import models

class Task(models.Model):
    """
    Represents a task in the to-do list.

    Attributes:
        text (str): The content or description of the task.
        completed (bool): A flag indicating whether the task has been completed. Defaults to False.
        created_at (datetime): The date and time when the task was created. Automatically set when the task is created.
    """
    text = models.CharField(max_length=255, help_text="Description of the task")
    completed = models.BooleanField(default=False, help_text="Status of the task, whether it is completed or not")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the task was created")

    def __str__(self):
        """
        Returns a string representation of the task.

        Returns:
            str: The description of the task.
        """
        return self.text
