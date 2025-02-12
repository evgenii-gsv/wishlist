from allauth.account.forms import PasswordField, SignupForm
from django import forms


class CustomSignupForm(SignupForm):
    error_css_class = 'error'

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Name',
    }))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'type': 'email',
            'placeholder': 'Email',
            'autocomplete': 'email',
        })
    )
    field_order = (
        'name',
        'email',
        'password1',
        'password2',
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.pop('autofocus', None)
        self.fields['password1'] = PasswordField(label='Password')
        self.fields['password2'] = PasswordField(label='Confirm password')

    def signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.save()
