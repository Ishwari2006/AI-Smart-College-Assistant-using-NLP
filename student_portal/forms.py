from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile


class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=6
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput
    )
    roll_number = forms.CharField(max_length=20)
    course = forms.CharField(max_length=100)
    semester = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data