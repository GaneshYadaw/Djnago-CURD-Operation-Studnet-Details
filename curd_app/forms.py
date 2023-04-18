from django import forms
from curd_app.models import Student



class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
        }