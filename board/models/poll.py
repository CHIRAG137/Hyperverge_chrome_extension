from django.db import models

class Poll(models.Model):
    """
    Represents a poll with a title and creation timestamp.

    Attributes:
        title (str): The title or question of the poll.
        created_at (datetime): The date and time when the poll was created. Automatically set when the poll is created.
    """
    title = models.CharField(max_length=255, help_text="Title or question of the poll")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the poll was created")

    def __str__(self):
        """
        Returns a string representation of the poll.

        Returns:
            str: The title of the poll.
        """
        return self.title

class PollOption(models.Model):
    """
    Represents an option or choice within a poll.

    Attributes:
        poll (ForeignKey): A reference to the related poll.
        option_text (str): The text of the poll option.
        votes (int): The number of votes the option has received. Defaults to 0.
    """
    poll = models.ForeignKey(Poll, related_name='options', on_delete=models.CASCADE, help_text="The poll to which this option belongs")
    option_text = models.CharField(max_length=255, help_text="Text of the poll option")
    votes = models.PositiveIntegerField(default=0, help_text="Number of votes received by this option")

    def __str__(self):
        """
        Returns a string representation of the poll option.

        Returns:
            str: The text of the poll option.
        """
        return self.option_text
