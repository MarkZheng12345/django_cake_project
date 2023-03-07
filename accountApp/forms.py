from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='*required')
    first_name = forms.CharField(max_length=30, required=True, help_text='*required')
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=30, required=True, help_text='required')
    phone_number = forms.CharField(max_length=10, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email aleady exists")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit():
            raise forms.ValidationError('enter a valid digits for phone number')

        return phone_number

