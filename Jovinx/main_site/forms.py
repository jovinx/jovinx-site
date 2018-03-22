
from django import forms
from django.forms import ModelForm
from .models import Message, ServiceRequest, Service, MailSubscriber


class ServiceRequstForm(ModelForm):

    SERVICES = Service.objects.all()
    SERVICE_LIST = []
    
    for data in SERVICES:
        service_tuple = (data.title, data.title)
        SERVICE_LIST.append(service_tuple)

    first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'First Name' }))
    last_name = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'Last Name' }))
    service_requested = forms.CharField(label='Service', max_length=200, widget=forms.Select(attrs={'class': 'form-control'}, choices=SERVICE_LIST))    
    phone = forms.IntegerField(label='Phone', widget=forms.NumberInput(attrs={ 'class': 'form-control', 'placeholder': 'Phone'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    specifications = forms.CharField(required=False, label='Specifications', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Describe your need. Leave blank if none for now'}))

    class Meta:
        model = ServiceRequest
        fields = ['first_name','last_name','phone','email','specifications', 'service_requested']        


class MessageForm(ModelForm):
    first_name = forms.CharField(label='First Name', max_length=50, widget=forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'First Name' }))
    last_name = forms.CharField(label='Last Name', max_length=50, widget=forms.TextInput(attrs={ 'class':'form-control', 'placeholder':'Last Name' }))
    phone = forms.IntegerField(label='Phone', widget=forms.NumberInput(attrs={ 'class': 'form-control', 'placeholder': 'Phone'}))
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Enter your Message'}))

    class Meta:
        model = Message
        fields = ['first_name','last_name','phone','email','message']


class NewsLetterForm(ModelForm):

    user_email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Enter your email'}))

    class Meta:
        model = MailSubscriber
        fields = ['user_email']
