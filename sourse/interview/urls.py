from django.urls import path

from interview.views import PollsView, CreatePollView, PollView, UpdatePoll, DeletePoll, CreateChoiceView, DeleteChoice, \
    UpdateChoice

urlpatterns = [
    path('', PollsView.as_view(), name="polls"),
    path('polls/add', CreatePollView.as_view(), name="poll-create"),
    path('polls/<int:pk>/view', PollView.as_view(), name="poll-view"),
    path('polls/<int:pk>/update', UpdatePoll.as_view(), name="poll-update"),
    path('polls/<int:pk>/delete', DeletePoll.as_view(), name="poll-delete"),
    path('polls/<int:pk>/answer/add', CreateChoiceView.as_view(), name="a-create"),
    path('answer/<int:pk>/update/', UpdateChoice.as_view(), name="a-update"),
    path('answer/<int:pk>/delete/', DeleteChoice.as_view(), name="a-delete"),

]
