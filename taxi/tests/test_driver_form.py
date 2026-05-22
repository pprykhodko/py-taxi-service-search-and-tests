from django.test import TestCase

from taxi.forms import DriverCreationForm


class DriverFormTests(TestCase):
    def test_driver_creation_form_with_additional_fields(self):
        form_data = {
            "username": "driver_username",
            "password1": "driver_password",
            "password2": "driver_password",
            "license_number": "ABC12345",
            "first_name": "driver_first_name",
            "last_name": "driver_last_name",
        }
        form = DriverCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
