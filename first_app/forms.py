from django import forms


class FormName(forms.Form):
    topic_name = forms.CharField()
    topic = forms.CharField(widget=forms.Textarea)
    name = forms.CharField()
    url = forms.CharField()
