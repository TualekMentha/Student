from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa']
        label = {
            'student_number': 'Student Number', 
            'first_name': 'First Name', 
            'last_name': 'Last Name', 
            'email': 'Email', 
            'field_of_study': 'Field of Study', 
            'gpa': 'GPA'
        }
        widget = {
            'student_number': forms.NumberInput(attrs={'class': 'from-control'}), 
            'first_name': forms.TextInput(attrs={'class': 'from-control'}), 
            'last_name': forms.TextInput(attrs={'class': 'from-control'}), 
            'email': forms.EmailInput(attrs={'class': 'from-control'}), 
            'field_of_study': forms.TextInput(attrs={'class': 'from-control'}), 
            'gpa': forms.NumberInput(attrs={'class': 'from-control'}),
        }