from django import forms

from .models import Url


class ShortUrlForm(forms.ModelForm):
    long_url = forms.URLField(label='Get your shorter link')

    class Meta:
        model = Url
        fields = ('long_url',)
