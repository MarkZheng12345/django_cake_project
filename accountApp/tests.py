from django.test import TestCase
from django.contrib.auth.models import User

from .forms import RegistrationForm
# Create your tests here.

class RegistrationFormTestCase(TestCase):
    def test_form_fields(self):
        form_data = {'first_name': 'f_name', 'last_name': 'l_name',
                     'email': 'email@gmail.com', 'username': 'username',
                     'phone_number': '1234567890',
                     'password1': 'pfirst_name1', 'password2': 'pfirst_name1'}

        reg_form = RegistrationForm(data=form_data)
        self.assertTrue(reg_form.is_valid())

    def test_invalid_email(self):
        form_data = {'first_name': 'f_name', 'last_name': 'l_name',
                     'email': 'emailgmail.com', 'username': 'username',
                     'phone_number': '1234567890',
                     'password1': 'pfirst_name1', 'password2': 'pfirst_name1'}

        reg_form = RegistrationForm(data=form_data)

        self.assertFalse(reg_form.is_valid())

    def test_user_already_exists(self):
        email = 'email@gmail.com'
        username = 'username8'
        form_data = {'first_name': 'f_name', 'last_name': 'l_name',
                     'email': email, 'username': username,
                     'phone_number': '1234567890',
                     'password1': 'pfirst_name1', 'password2': 'pfirst_name1'}

        User.objects.create_user(username=username,
                                 email=email,
                                 password='password1',
                                 first_name='first_name',
                                 last_name='last_name')
        reg_form = RegistrationForm(data=form_data)

        self.assertFalse(reg_form.is_valid())

    def test_blank_field(self):
        email = 'email9@gmail.com'
        username = 'username9'
        form_data = {'first_name': '', 'last_name': None,
                     'email': email, 'username': username,
                     'phone_number': '1234567890',
                     'password1': 'pfirst_name', 'password2': 'pfirst_name'}
        reg_form = RegistrationForm(data=form_data)
        if reg_form.errors:
            for field in reg_form:
                for error in field.errors:
                    print(field.label, error)
        self.assertFalse(reg_form.is_valid())