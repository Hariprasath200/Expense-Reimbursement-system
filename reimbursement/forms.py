from django import forms

class Emp(forms.Form):
    employee_name = forms.CharField(max_length=100)
    employee_code = forms.CharField(max_length=20)
    mobile_number = forms.CharField(max_length=15)  # Assuming maximum length of mobile number is 15 characters
    email = forms.EmailField()
    upload = forms.FileField()
    description = forms.CharField(widget=forms.Textarea)
