from django import forms
from .models import Student



class Valueform(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name', 
            'age',
            'email', 
            'gender'
        ]