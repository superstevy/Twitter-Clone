from django import forms
from .models import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = '__all__'
        widgets = {
            'body': forms.Textarea()
        }
