from django import forms

class InputForm(forms.Form):
    input_value = forms.CharField()
    