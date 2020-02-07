from django import forms
from management.models import USER, Destination, Gallery


class userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = USER
        fields = "__all__"


class destinationform(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Destination
        fields = "__all__"


class galleryform(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Gallery
        fields = "__all__"


class login(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailField)
    password = forms.PasswordInput()

    class Meta:
        model = USER
        fields = "__all__"
