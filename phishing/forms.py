from django import forms
from .models import credentials

class credentials_capturer(forms.ModelForm):
    class Meta:
        model = credentials
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].initial = ''
        self.fields['password'].initial = ''    