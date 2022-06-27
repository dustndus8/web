from django import forms

from accounts.models import ProfileImage


class ProfileFormImage(forms.ModelForm):
    class Meta:
        model = ProfileImage
        fields = ('image',)