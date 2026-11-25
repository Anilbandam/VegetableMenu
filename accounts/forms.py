from django  import forms
class details(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)
    confirm_password=forms.CharField(max_length=20)
    email=forms.EmailField()