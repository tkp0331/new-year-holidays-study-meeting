from django import forms
from .models import Student, Faculty


class EntryForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('faculty_id', 'name', 'email')


class FacultyForm(forms.ModelForm):
    pass
