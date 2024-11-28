from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone_number']
        
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': '성함을 입력해주세요'}))
    phone_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': '010-0000-0000'}))