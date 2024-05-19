from django import forms


class MyInputForm(forms.Form):
    data = forms.CharField(max_length=100)
