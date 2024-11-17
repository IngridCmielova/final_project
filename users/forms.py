from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='E-mail')
    first_name = forms.CharField(label='Jméno')
    last_name = forms.CharField(label='Příjmení')

    username = forms.CharField(
        label='Uživatelské jméno',
        help_text='Povinné. 150 znaků nebo méně. Pouze písmena, číslice a znaky @/./+/-/_.',
        max_length=150
    )

    password1 = forms.CharField(
        label='Heslo',
        widget=forms.PasswordInput,
        help_text='Vaše heslo musí obsahovat alespoň 8 znaků, nesmí být běžné a nesmí být zcela číselné.'
    )
    password2 = forms.CharField(
        label='Potvrzení hesla',
        widget=forms.PasswordInput,
        help_text='Zadejte stejné heslo jako výše, pro ověření.'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        labels = {
            'username': 'Uživatelské jméno',
            'password1': 'Heslo',
            'password2': 'Potvrzení hesla',
        }


class ChangePasswordForm(PasswordChangeForm):
    """A form to handle user password changes with customized input fields."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget = forms.PasswordInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Staré heslo'})
        self.fields['new_password1'].widget = forms.PasswordInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Nové heslo'})
        self.fields['new_password2'].widget = forms.PasswordInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Potvrď nové heslo'})


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Uživatelské jméno',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Heslo',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
