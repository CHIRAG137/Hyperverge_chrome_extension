from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views import View
import google.generativeai as genai
from django.conf import settings

def get_gemini_model():
    """
    Configures and returns a Gemini generative model instance for chat.

    Returns:
        genai.GenerativeModel: An instance of the Gemini generative model configured for chat.
    """
    api_key = settings.GEMINI_API_KEY
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    return model.start_chat(history=[])

# Initialize the chat model and history
chat = get_gemini_model()
chat_history = []

@method_decorator(csrf_exempt, name='dispatch')
class ChatView(View):
    """
    A view to handle chat requests with the Gemini model.

    Methods:
        post: Handles POST requests to interact with the chat model.
    """
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests to the chat view.

        Args:
            request (HttpRequest): The incoming request object.

        Returns:
            JsonResponse: A JSON response containing the chat bot's reply or an error message.
        """
        try:
            user_input = request.POST.get('user_input')
            if user_input:
                # Send the user input to the chat model and get the response
                response = chat.send_message(user_input)
                # Update chat history with the latest interaction
                chat_history.append({"user": user_input, "bot": response.text})
                return JsonResponse({"response": response.text})
            else:
                return JsonResponse({"error": "No user input provided."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
