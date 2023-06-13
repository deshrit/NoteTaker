from django import forms
from .models import Note

class TakeNoteForm(forms.Form):
    title = forms.CharField(
        required=False,
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Title ...'
        }),
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Note ...'
        }),
    )

class UpdateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "body"]
        widgets = {
            'title': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Title ...'
                }
            ),
            'body': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Body ...'
                }
            )
        }