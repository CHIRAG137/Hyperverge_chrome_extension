import requests
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from geopy.geocoders import Nominatim
from board.serializers.waether import WeatherSerializer

class WeatherAPIView(APIView):
    """
    API view to fetch and return weather data for a given city.

    This view handles GET requests to retrieve the current weather for a specified city.
    It uses the OpenWeatherMap API to fetch the weather data and Geopy to get coordinates
    for the city.

    Methods:
        get(request, *args, **kwargs): Handles GET requests to return weather data or an error message.
    """

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve weather information for a city.

        This method extracts the city name from the request, retrieves its coordinates using
        the Geopy Nominatim geocoder, and then fetches weather data from the OpenWeatherMap API.
        It returns a JSON response containing the city name, temperature, and weather description,
        or an error message if the city is not found or if there is an issue with the API request.

        Args:
            request (HttpRequest): The incoming HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A JSON response with weather data or an error message.
        """
        city = request.query_params.get('city', 'Ranchi')  # Default to Ranchi if no city is provided

        # Get coordinates for the city
        geolocator = Nominatim(user_agent="weather_api")
        location = geolocator.geocode(city)
        
        if not location:
            return Response({'error': 'City not found'}, status=400)

        latitude = location.latitude
        longitude = location.longitude

        # Fetch weather data
        api_key = settings.WEATHER_API_KEY
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
        
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        if weather_response.status_code == 200:
            city_name = weather_data['name']
            temperature = weather_data['main']['temp']
            weather_description = weather_data['weather'][0]['description']
            
            weather_response_data = {
                'city': city_name,
                'temperature': temperature,
                'weather': weather_description
            }
            
            serializer = WeatherSerializer(weather_response_data)
            return Response(serializer.data)
        else:
            return Response({'error': 'Weather API error'}, status=400)
