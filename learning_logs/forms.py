from dataclasses import fields
from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    # Nest a Meta class to tell Django on which model to base the form on 
    # and which fields to include in the form.
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

