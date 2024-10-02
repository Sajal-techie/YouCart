from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser


class SignupForm(forms.ModelForm):
    password2 = forms.CharField()


    class Meta:
        model = CustomUser
        fields = ['username','email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        validate_email(email)
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)
        return password
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        print(password,password2)
        if password and password != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  
        if commit:
            user.save()
        return user
    