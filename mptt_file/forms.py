from mptt.forms import forms
from .models import FileObject


class AddFileForm(forms.Form):
    name = forms.CharField(max_length=50, help_text='*Required')
    parent = forms.ModelChoiceField(queryset=FileObject.objects.all())
