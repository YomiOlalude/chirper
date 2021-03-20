from .models import *
from django import forms

MAX_LENGTH = 280

class ChirpCreateForm(forms.ModelForm):
    class Meta:
        model = Chirp
        fields = ["content"]
        
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_LENGTH:
            raise forms.ValidationError("Sorry, this chirp is too long")
        return content
        