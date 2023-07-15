from django import forms
from django.contrib.auth.models import User
from datetime import date, datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm as DefaultPasswordChangeForm
from django.contrib.auth import get_user_model
from .models import Appointment, TATTOO_LOCATION, APPOINTMENT_STATUS, TATTOO_CATEGORY, TATTOO_SIZE, Artist


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=16,
                                 required=True,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-input',
                                     'autocomplete': 'off',
                                 }
                                 ))
    last_name = forms.CharField(max_length=16,
                                required=False,
                                widget=forms.TextInput(attrs={'class': 'form-input',
                                                              'autocomplete': 'off', }))
    username = forms.CharField(max_length=20,
                               required=False,
                               widget=forms.TextInput(attrs={'class': 'form-input',
                                                             'autocomplete': 'off', }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


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
        self.fields['new_password2'].widget.attrs.update({
            'autocomplete': 'off',
            'class': 'form-input'
        })


class DateTimeInputPicker(forms.DateTimeInput):
    input_type = 'datetime-local'
    format = '%Y-%m-%dT%H:%M'
    attrs = {'step': '1'}


class AppointmentForm(forms.ModelForm):
    appointment_at = forms.DateTimeField(initial=datetime.now(), widget=forms.DateTimeInput(
        attrs={
            'class': 'form-input'
        }))
    tattoo_location = forms.ChoiceField(choices=TATTOO_LOCATION,
                                        required=True,
                                        widget=forms.Select(attrs={
                                           'class': 'form-input'}))
    tattoo_size = forms.ChoiceField(choices=TATTOO_SIZE,
                                    required=True,
                                    widget=forms.Select(attrs={
                                       'class': 'form-input'}))
    tattoo_category = forms.ChoiceField(choices=TATTOO_CATEGORY,
                                        required=True,
                                        widget=forms.Select(attrs={
                                            'class': 'form-input'}))
    artist = forms.ModelChoiceField(queryset=Artist.objects.all(),
                                    required=True,
                                    widget=forms.Select(attrs={
                                        'class': 'form-input'}))

    class Meta:
        model = Appointment
        fields = ['appointment_at', 'tattoo_location',
                  'tattoo_size', 'tattoo_category', 'artist']
