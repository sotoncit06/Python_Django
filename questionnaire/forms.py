from django import forms
from . import models

class CreateQuestions(forms.ModelForm):
    class Meta:
        model= models.Questionnaire
        fields=['question', 'answar']