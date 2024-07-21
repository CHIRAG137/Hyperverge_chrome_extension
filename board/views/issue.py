from rest_framework import generics
from board.models.issue import Issue
from board.serializers.issue import IssueSerializer

class IssueListCreateView(generics.ListCreateAPIView):
    """
    A view to list all Issue instances and create new Issue instances.

    This view uses the `ListCreateAPIView` generic class from Django REST framework to
    provide functionality for listing all issues and creating new ones. After creating
    an issue, it also submits the issue details to a Google Sheets document.

    Attributes:
        queryset (QuerySet): The queryset of Issue instances to be listed or created.
        serializer_class (Serializer): The serializer class used to validate and serialize the data.
    """
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

    def perform_create(self, serializer):
        """
        Save the new issue and submit its details to Google Sheets.

        Args:
            serializer (Serializer): The serializer instance used to save the issue.

        Calls:
            submit_to_google_sheets(issue): Function to submit the issue details to Google Sheets.
        """
        issue = serializer.save()
        submit_to_google_sheets(issue)

import os.path
from google.oauth2 import service_account
from googleapiclient.discovery import build

def submit_to_google_sheets(issue):
    """
    Submits the details of an Issue instance to a Google Sheets document.

    This function authenticates with Google Sheets API using a service account, then appends
    the issue details to a specified range in a Google Sheets document.

    Args:
        issue (Issue): The Issue instance whose details will be submitted to Google Sheets.

    Raises:
        Exception: If there is an error during authentication or while calling the Google Sheets API.
    """
    # Path to your service account key file
    SERVICE_ACCOUNT_FILE = 'C:/Users/chira/Downloads/hyperverge-430105-243e3cc0b037.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    # Authenticate and construct service.
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)

    # The ID and range of the spreadsheet.
    SPREADSHEET_ID = '1ahAMkVeCtTcQ164DCryDdSrOGUDxpY8zxYjdYm9rSzs'
    RANGE_NAME = 'Sheet1!A1'

    # The data to insert
    values = [
        [
            str(issue.id), issue.title, issue.description, str(issue.created_at)
        ],
    ]
    body = {
        'values': values
    }

    # Call the Sheets API to append the data
    sheet = service.spreadsheets()
    result = sheet.values().append(
        spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME,
        valueInputOption='RAW', body=body).execute()

    # Optional: You might want to handle or log the result of the operation
    print(f"Updated {result.get('updates').get('updatedCells')} cells.")

