from django import forms
from .models import question

class question_form(forms.ModelForm):
  name = forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control',
    'id':'name',
    'placeholder':'Enter your name'
  }),max_length=100,required=True)

  emailid = forms.EmailField(widget=forms.EmailInput(attrs={
    'class':'form-control',
    'id':'exampleInputEmail1',
    'aria-describedby':'emailHelp',
    'placeholder':'Enter email..'
  }),max_length=100,required=True)

  subject = forms.CharField(widget=forms.TextInput(attrs={
    'class':'form-control',
    'id':'subject',
    'placeholder':'Enter subject name..'
  }),max_length=100,required=True)

  answer = forms.CharField(widget=forms.Textarea(attrs={
    'class':'form-control',
    'id':'question',
    'rows':'4',
    'placeholder':'Enter your question here..',
    'aria-describedby':'questionhelp'

  }))

  class Meta():
    model = question
    fields = ['name','emailid','subject','answer']

