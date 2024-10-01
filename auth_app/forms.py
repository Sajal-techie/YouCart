from django import forms
from .models import CustomUser


class SignupForm(forms.ModelForm):
    password2 = forms.CharField()


    class Meta:
        model = CustomUser
        fields = ['username','email', 'password']


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
    