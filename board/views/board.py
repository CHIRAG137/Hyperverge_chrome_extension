from django.shortcuts import render
from django.http import JsonResponse
from board.models.board import Notice
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from board.serializers.board import NoticeSerializer

@csrf_exempt
def notice_board(request):
    """
    Handle GET and POST requests for the notice board.

    For GET requests, this view fetches all notices from the database, orders them
    by creation date in descending order, and renders them to the 'notice.html' template.

    For POST requests, this view parses the incoming JSON data, validates it, and
    saves a new notice to the database if the data is valid.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A rendered HTML page for GET requests.
        JsonResponse: A JSON response with the created notice data for valid POST requests,
                      or a JSON response with errors for invalid POST requests.
    """
    if request.method == 'GET':
        # Fetch all notices from the database and order them by creation date (newest first)
        notices = Notice.objects.all().order_by('-created_at')
        # Render the 'notice.html' template with the fetched notices
        return render(request, 'notice.html', {'notices': notices})
    
    elif request.method == 'POST':
        # Parse the incoming JSON data
        data = JSONParser().parse(request)
        # Deserialize the data into a Notice instance
        serializer = NoticeSerializer(data=data)
        if serializer.is_valid():
            # Save the new notice to the database if the data is valid
            serializer.save()
            # Return a JSON response with the created notice data
            return JsonResponse(serializer.data, status=201)
        # Return a JSON response with errors if the data is invalid
        return JsonResponse(serializer.errors, status=400)

# Example usage:
# - To fetch all notices (GET request): Send a GET request to the URL mapped to the 'notice_board' view.
# - To create a new notice (POST request): Send a POST request with JSON data to the same URL.
#   Example JSON data: {"title": "New Notice", "message": "This is the content of the new notice."}
