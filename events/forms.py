from django import forms

class ConsultForm(forms.Form):
    full_name = forms.CharField(max_length=75, widget=forms.TextInput(attrs={"placeholder": "Full name", "required": "true"}))
    your_mail = forms.EmailField(max_length=75, widget=forms.EmailField(attrs={"placeholder": "Email Address", "required": "true"}))
    subject = forms.CharField(max_length=150, widget=forms.TextInput(attrs={"placeholder": "Subject", "required": "true"}))
    your_message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Your Message (optional)","rows": "6", "required": "false"}))


class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=75, widget=forms.TextInput(attrs={"placeholder": "Full name", "required": "true"}))
    your_mail = forms.EmailField(max_length=75, widget=forms.EmailField(attrs={"placeholder": "Email Address", "required": "true"}))
    company_name = forms.CharField(max_length=75, widget=forms.TextInput(attrs={"placeholder": "Company Name", "required": "true"}))
    your_message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Your Message","rows": "6", "required": "true"}))

class RegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=75, widget=forms.TextInput(attrs={"placeholder": "Full Name", "required": "true"}))
    your_mail = forms.EmailField(max_length=75, widget=forms.EmailField(attrs={"placeholder": "Email Address", "required": "true"}))
    address = forms.CharField(max_length=225, widget=forms.TextInput(attrs={"placeholder": "Your Address", "required": "true"}))
    phone_number = forms.CharField(max_length=11, widget=forms.NumberInput(attrs={"placeholder": "Phone Number(090xxxxxxxx)", "required": "true"}))
    company_name = forms.CharField(max_length=75, widget=forms.TextInput(attrs={"placeholder": "Company Name(If employed)", "required": "false"}))
    position = forms.CharField(max_length=75, widget=forms.TextInput(attrs={"placeholder": "Position (if employed)", "required": "false"}))
    