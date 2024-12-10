from django import forms
from .models import reader

class ReturnsForm(forms.Form):
    reader_id = forms.ModelChoiceField(queryset=reader.objects.all(), label="Select Reader")
    borrow_date = forms.DateField(widget=forms.SelectDateWidget(), label="Borrow Date")
    return_date = forms.DateField(widget=forms.SelectDateWidget(), label="Return Date")
