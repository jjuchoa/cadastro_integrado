from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserForm(forms.Form):
    password = forms.CharField(max_length=128)
    last_login = forms.DateTimeField(blank=True, null=True)
    is_superuser = forms.BooleanField()
    username = forms.CharField(unique=True, max_length=150)
    first_name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=254)
    is_staff = forms.BooleanField()
    is_active = forms.BooleanField()
    date_joined = forms.DateTimeField()
    last_name = forms.CharField(max_length=150)

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar Usuário'))
