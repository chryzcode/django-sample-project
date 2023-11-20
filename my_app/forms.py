from django import forms
from .models import Note

#create a form based on the Note model
class noteForm(forms.ModelForm):
    class Meta:
        model = Note
        #form fields/inputs that will be shown
        fields = ['title', 'body']
        #added a css class and html placeholder to the form inputs
        #the form-control css class is from bootstrap
        widgets={
                'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Note title'}),
                'body':forms.Textarea(attrs={'class':'form-control',  'placeholder':'Start writing...'}),
        }