from django.urls import path
from board.views.board import notice_board
from board.views.chatgpt import ChatView
from board.views.checklist import TaskListCreateView, TaskUpdateView
from board.views.gmeet import generate_meet_link
from board.views.issue import IssueListCreateView
from board.views.poll import PollDetailAPIView, PollListCreateAPIView
from board.views.weather import WeatherAPIView

urlpatterns = [
    path('notice/', notice_board, name='notice_board'),
    path('poll/', PollListCreateAPIView.as_view(), name='poll-list-create'),
    path('poll/<int:pk>/', PollDetailAPIView.as_view(), name='poll-detail'),
    path('issues/', IssueListCreateView.as_view(), name='issue_list_create'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    path('generate-meet-link/', generate_meet_link, name='generate_meet_link'),
    path('chat/', ChatView.as_view(), name='chat_endpoint'),
    path('geolocation/', WeatherAPIView.as_view(), name='ip-geolocation'),
]
