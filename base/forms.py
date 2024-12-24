from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Medicine



class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']






# Product Form
class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = ['product_image','name','description','manufacture_date','expiry_date','price']
        # Listing all the fields that will enable as editable in form.
        labels = {
            'product_image' : 'Product Image',
            'name':  '',
            'description':  '',
            'manufacture_date':  '',
            'expiry_date':  '',
            'price':  ''
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Product Name'}),
            'description':forms.TextInput(attrs={'class' : 'form-control','placeholder' : 'Product Description'}),
            'manufacture_date':forms.DateInput(attrs={'class' : 'form-control','placeholder': 'Manufacture Date -- YYYY-MM-DD'}),
            'expiry_date':forms.DateInput(attrs={'class' : 'form-control', 'placeholder': 'Expiry Date -- YYYY-MM-DD'}),
            'price':forms.NumberInput(attrs={'class' : 'form-control','placeholder' : 'Price -- 0000.00'}),
            
        }
        
        
        
