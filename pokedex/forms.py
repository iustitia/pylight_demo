from django import forms


class AddForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    is_yellow = forms.BooleanField(label="Yellow")
