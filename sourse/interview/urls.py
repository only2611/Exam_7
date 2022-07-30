from django.urls import path

from interview.views import PollsView, CreatePollView, PollView, UpdatePoll, DeletePoll

urlpatterns = [
    # path('tasks/', IndexView.as_view(), name="index_view"),
    # path('tasks/create', CreateTaskView2.as_view(), name="create2"),
    # path('task/<int:pk>/', TaskView.as_view(), name="task_view"),
    # path('project/<int:pk>/task/create', CreateTaskView.as_view(), name="create"),
    # path('task/<int:pk>/update', UpdateTask.as_view(), name="update"),
    # path('task/<int:pk>/delete', DeleteTask.as_view(), name="delete"),
    path('', PollsView.as_view(), name="polls"),
    path('polls/add', CreatePollView.as_view(), name="poll-create"),
    path('polls/<int:pk>/view', PollView.as_view(), name="poll-view"),
    path('polls/<int:pk>/update', UpdatePoll.as_view(), name="poll-update"),
    path('polls/<int:pk>/delete', DeletePoll.as_view(), name="poll-delete"),

]
