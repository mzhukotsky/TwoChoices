from django import forms
from django.utils import timezone

class CreatePollForm(forms.Form):
    question = forms.CharField(max_length=200, label='Question')
    choices = forms.CharField(
        label='Choices (comma separated)', 
        widget=forms.Textarea(attrs={'rows': 3})
    )
    pub_date = forms.DateTimeField(widget=forms.HiddenInput(), initial=timezone.now())