from django import forms


class InputForm(forms.Form):
    title = forms.CharField(max_length=200)
    text = forms.CharField(max_length=200)

