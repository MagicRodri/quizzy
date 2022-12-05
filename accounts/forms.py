from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()

class LoginForm(AuthenticationForm):


    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':"username",
                    'placeholder':'Username' 
                }
            )
        self.fields['password'].widget = forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id':"password",
                'placeholder':'Password' 
            }
        )
    class Meta:
        model = User
        fields = '__all__'

class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(
                attrs={
                    'class':'form-control',
                    'id':"username",
                    'placeholder':'Username' 
                }
            )
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id':"password1",
                'placeholder':'Password' 
            }
        )
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={
                'class':'form-control',
                'id':"password2",
                'placeholder':'Confirm password' 
            }
        )
    class Meta:
        model = User
        fields = ['username',]
