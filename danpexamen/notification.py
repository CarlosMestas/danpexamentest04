from django import forms


class InputForm(forms.Form):
    title = forms.CharField(max_length=200)
    info = forms.CharField(max_length=200)

