from django.forms import Form
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from interview.forms import ChoiceForm, AForm
from interview.models import Choice, Poll, Answering


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


class CreateView(View):
    def get(self, request, **kwargs):
        if request.method == "GET":
            form = AForm()
            return render(request, "answers/answering.html", {"form": form})
    def post(self, request):
            form = AForm(data=request.POST)
            if form.is_valid():
                polls = form.cleaned_data.get("polls")
                variantes = form.cleaned_data.get("variantes")
                new_task = Answering.objects.create(variantes=variantes, polls=polls)
                return redirect("polls", )
            return render(request, "answers/answering.html", {"form": form})
