from .models import *
from django import forms
from django.conf import settings

MAX_CHIRP_LENGTH = settings.MAX_CHIRP_LENGTH


class ChirpCreateForm(forms.ModelForm):
    class Meta:
        model = Chirp
        fields = ["content"]
        
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_CHIRP_LENGTH:
            raise forms.ValidationError("Sorry, this chirp is too long")
        return content
        