from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm as DefaultPasswordChangeForm
from core.models import GENDER

User = get_user_model()


class RegistrationForm(forms.ModelForm):

    username = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'form-input', 'autocomplete': 'off'}))

    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-input',
                                                           'placeholder': 'email@email.com',
                                                           'autocomplete': 'off', }))
    first_name = forms.CharField(max_length=16,
                                 required=True,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-input',
                                     'placeholder': 'John',
                                     'autocomplete': 'off',
                                 }
                                 ))
    last_name = forms.CharField(max_length=16,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'form-input',
                                                              'placeholder': 'Smith',
                                                              'autocomplete': 'off', }))

    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': '', 'autocomplete': 'off', 'class': 'form-input'}))

    age = forms.IntegerField(required=True,
                             min_value=18,
                             max_value=100,
                             widget=forms.NumberInput(attrs={'class': 'form-input',
                                                             'placeholder': '18',
                                                             'autocomplete': 'off',
                                                             }))

    gender = forms.ChoiceField(choices=GENDER,
                               required=False,
                               widget=forms.Select(attrs={
                                   'class': ' form-input'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age', 'gender']

    def clean_username(self):
        username_input = self.cleaned_data.get('username')
        if User.objects.filter(username=username_input).exists():
            raise forms.ValidationError("Username already exists!")
        return username_input

    def clean_email(self):
        email_input = self.cleaned_data.get('email')
        if User.objects.filter(email=email_input).exists():
            raise forms.ValidationError("Email already exists!")

        return email_input


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-input',
                                                           'placeholder': 'email@email.com',
                                                           'autocomplete': 'off',
                                                           }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '********',
                                                                 'autocomplete': 'off',
                                                                 'class': 'form-input'
                                                                 }))


class PasswordChangeForm(DefaultPasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        self.fields['old_password'].widget.attrs.update({
            'autocomplete': 'off',
            'class': 'form-input'
        })
        self.fields['new_password1'].widget.attrs.update({
            'autocomplete': 'off',
            'class': 'form-input'
        })
        self.fields['new_password2'].widget = forms.TextInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-input',
        })