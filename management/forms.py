from django import forms
from management.models import USER


class userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = USER
        fields = "__all__"


class login(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailField)
    password = forms.PasswordInput()

    class Meta:
        model = USER
        fields = "__all__"
