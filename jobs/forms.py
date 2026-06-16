from django import forms
from .models import JobApplication
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication

        fields = [
            'company_name',
            'job_title',
            'job_location',
            'applied_date',
            'status',
            'notes'
        ]

        widgets = {

            'company_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter company name'
                }
            ),

            'job_title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter job title'
                }
            ),

            'job_location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter location'
                }
            ),

            'applied_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'status': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'notes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Add notes about this application'
                }
            )
        }

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2'
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter username'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm password'
        })