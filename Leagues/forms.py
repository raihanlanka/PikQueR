from django import forms
from .models import FreeLeagueChat
from django.core.exceptions import ValidationError



class FreeLeagueChatForm(forms.ModelForm):

    class Meta:
        model = FreeLeagueChat
        fields = ('text',)