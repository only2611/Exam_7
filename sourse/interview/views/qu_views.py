from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from interview.forms import PollForm
from interview.models import Poll


class PollsView(ListView):
    model = Poll
    template_name = "questions/index.html"
    context_object_name = "polls"
    ordering = ("-created_at")
    paginate_by = 5



class CreatePollView(CreateView):
    form_class = PollForm
    template_name = "questions/new-question.html"


    def get_success_url(self):
        # return reverse("p-view", kwargs={"pk": self.object.pk})
        return reverse("polls",)



class PollView(DetailView):
    template_name = "questions/poll.html"
    model = Poll



class UpdatePoll(UpdateView):
    form_class = PollForm
    template_name = "questions/update_poll.html"
    model = Poll


    # def get_success_url(self):
    #     return reverse("project-view", kwargs={"pk": self.object.pk})


class DeletePoll(DeleteView):
    model = Poll
    template_name = "questions/delete_poll.html"
    success_url = reverse_lazy("polls")