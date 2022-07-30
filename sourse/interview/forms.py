from django import forms
from django.forms import widgets

from interview.models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ["question"]


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['variant',]