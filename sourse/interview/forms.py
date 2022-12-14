from django import forms
from django.forms import widgets

from interview.models import Poll, Choice, Answering


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ["question"]


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['variant',]


class AForm(forms.Form):
    polls = forms.ModelChoiceField(queryset=Poll.objects.all())
    variantes = forms.ModelChoiceField(queryset=Choice.objects.all())

