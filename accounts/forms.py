from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder' : 'username'
        }),
        label=''
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Email Address'
        }),
        label=''
    )
    first_name = forms.CharField(max_length=50,
        widget=forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'First Name',
        }),
        label=''
    )
    last_name = forms.CharField(max_length=50,
        widget=forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder' : 'Last Name'
        }),label=""
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder ': "Password"
            }),
        label='',
        
        error_messages={
            'required': '',
        }
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder ': "Confirm Password"
            }),
        label='',
        error_messages={
            'required': '',
        }
    )
    
    
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email',"password1",'password2']
        labels = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'password1': '',
            'password2': '',
        }
        
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm,self).__init__( *args, **kwargs)
        
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['error_messages'] = ''