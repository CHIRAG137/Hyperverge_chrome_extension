from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    """
    Serializer for weather information.

    Attributes:
        city (str): The name of the city for which the weather information is provided.
        temperature (float): The temperature in degrees Celsius (or other specified unit).
        weather (str): A description of the weather conditions (e.g., sunny, cloudy).
    """
    city = serializers.CharField(
        max_length=100,
        help_text="The name of the city for which the weather information is provided"
    )
    temperature = serializers.FloatField(
        help_text="The temperature in degrees Celsius (or other specified unit)"
    )
    weather = serializers.CharField(
        max_length=100,
        help_text="A description of the weather conditions (e.g., sunny, cloudy)"
    )

    def validate_temperature(self, value):
        """
        Validate the 'temperature' field to ensure it is a realistic value.

        Args:
            value (float): The temperature value to be validated.

        Returns:
            float: The validated temperature value.

        Raises:
            serializers.ValidationError: If the temperature value is unrealistic or invalid.
        """
        if value < -100 or value > 60:
            raise serializers.ValidationError("Temperature value is out of realistic range.")
        return value

    def validate_weather(self, value):
        """
        Validate the 'weather' field to ensure it is not empty.

        Args:
            value (str): The weather description to be validated.

        Returns:
            str: The validated weather description.

        Raises:
            serializers.ValidationError: If the weather description is empty or invalid.
        """
        if not value.strip():
            raise serializers.ValidationError("Weather description cannot be empty.")
        return value
