from django import forms

from .models import Classification

class ClassificationForm(forms.ModelForm):
    classification = forms.IntegerField(label="Classification", min_value=1, max_value=5)
    comment = forms.CharField(label="Comment", widget=forms.Textarea, required=False)
