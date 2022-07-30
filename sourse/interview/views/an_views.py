from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from interview.forms import ChoiceForm
from interview.models import Choice, Poll


# class IndexView(ListView):
#     model = Choice
#     template_name =
#     context_object_name = "tasks"
#     ordering = ("-updated_at")
#     paginate_by = 7


class CreateChoiceView(CreateView):
    model = Choice
    form_class = ChoiceForm
    template_name = "answers/create.html"


    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get("pk"))
        form.instance.poll = poll
        return super().form_valid(form)

    def get_success_url(self):
       return reverse("poll-view", kwargs={"pk": self.object.poll.pk})


class UpdateChoice(UpdateView):
    form_class = ChoiceForm
    template_name = "answers/update.html"
    model = Choice


    def get_success_url(self):
        return reverse("poll-view", kwargs={"pk": self.object.poll.pk})



class DeleteChoice(DeleteView):
    model = Choice
    template_name = "answers/delete.html"
    # success_url = reverse_lazy("poll-view")

    def get_success_url(self):
        return reverse("poll-view", kwargs={"pk": self.object.poll.pk})