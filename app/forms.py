from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Candidate, Company,Job, Application

class Signupforms(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password(Again)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'username': 'Username', 'first_name': 'First Name', 'last_name': 'Last Name', 'email': 'Email Address'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}), 
        'first_name': forms.TextInput(attrs={'class': 'form-control'}),
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),}

class loginForms(AuthenticationForm):
    username =forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'True'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CandidateForms(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['stud_name', 'address', 'mobile', 'class_12', 'class_10', 'persuing', 'pro_img', 'experience', 'cv']
        labels = {
            'stud_name': 'Name',
            'address': 'Address',
            'mobile': 'Mobile Number',
            'class_12': 'Class 12 aggregate',
            'class_10': 'Class 10 aggregate',
            'persuing': 'Persue Course Currently',
            'pro_img': 'Upload Your image',
            'experience': 'Experience(if any)',
            'cv': 'Upload Resume',
        }
        widgets = {
            'stud_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'class_12': forms.NumberInput(attrs={'class': 'form-control'}),
            'class_10': forms.NumberInput(attrs={'class': 'form-control'}),
            'persuing': forms.Select(attrs={'class': 'form-control'}),
            'pro_img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'experience': forms.Textarea(attrs={'class': 'form-control'}),
            'cv': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'desc']
        labels = {'name': 'Company Name',
        'desc': 'Description'}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}), 
        'desc': forms.Textarea(attrs={'class': 'form-control'})}

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'skills', 'duration', 'activities', 'perks', 'amount']
        labels = {
            'title': 'Choose Job Post',
            'skills': 'Add skills required',
            'duration': 'Add Duration of Internship',
            'activities': 'Day to day activities',
            'perks': 'Add perks',
            'amount': 'Add Amount to be paid',
        }
        widgets = {
            'title': forms.Select(attrs={'class': 'form-control'}),
            'skills': forms.Textarea(attrs={'class':'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'activities': forms.Textarea(attrs={'class': 'form-control'}),
            'perks': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['objective', 'reason']
        labels = {
            'objective': 'What are your goals ? ',
            'reason': 'Why do you want to do this internship ?'
        }
        widgets = {
            'objective': forms.TextInput(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(attrs={'class': 'form-control'})
        }
        