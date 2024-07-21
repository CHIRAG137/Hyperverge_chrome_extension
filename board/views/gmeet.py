from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import datetime

# Define the correct scope and credentials for Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'C:/Users/chira/Downloads/hyperverge-430105-fd07cc048bbe.json'

@csrf_exempt
def generate_meet_link(request):
    """
    Generates a Google Meet link by creating a calendar event with conference data.

    This view handles POST requests to create a Google Calendar event with a Google Meet link.
    The event is scheduled to start 10 minutes from the current UTC time and lasts for 1 hour.

    Args:
        request (HttpRequest): The incoming HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the Google Meet link or an error message.

    Raises:
        HttpError: If there is an issue with the Google Calendar API request.
        Exception: For any other errors that occur during the process.
    """
    if request.method == 'POST':
        try:
            # Load credentials and create a service object for the Google Calendar API
            credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES
            )
            service = build('calendar', 'v3', credentials=credentials)

            # Define the event with Google Meet conference data
            event = {
                'summary': 'Meeting',
                'description': 'A chance to hear more about Google Meet.',
                'start': {
                    'dateTime': (datetime.datetime.utcnow() + datetime.timedelta(minutes=10)).isoformat(),
                    'timeZone': 'UTC',
                },
                'end': {
                    'dateTime': (datetime.datetime.utcnow() + datetime.timedelta(hours=1)).isoformat(),
                    'timeZone': 'UTC',
                },
                'conferenceData': {
                    'createRequest': {
                        'requestId': 'random-string',  # Ensure this ID is unique for each request
                        'conferenceSolutionKey': {
                            'type': 'hangoutsMeet',
                        },
                    },
                },
                'attendees': [],
            }

            # Create the event with the conference data in the Google Calendar
            event = service.events().insert(
                calendarId='primary',
                body=event,
                conferenceDataVersion=1
            ).execute()

            # Extract the Google Meet link from the event response
            meet_link = event.get('conferenceData', {}).get('entryPoints', [{}])[0].get('uri', '')

            return JsonResponse({'meet_link': meet_link}, status=200)
        except HttpError as e:
            return JsonResponse({'error': f'HttpError: {e}'}, status=500)
        except Exception as e:
            return JsonResponse({'error': f'Error: {e}'}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
