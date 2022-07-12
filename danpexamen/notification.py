from django import forms


class InputForm(forms.Form):
    title = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "input"}))
    text = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': "input"}))

