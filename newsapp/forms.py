from django import forms

class registration(forms.Form):
    name= forms.CharField(widget=forms.TextInput
                          (attrs={'placeholder': 'Enter Your Full Name'}))
    email= forms.EmailField(widget=forms.TextInput
                            (attrs={'placeholder':'Enter Your Email'}))
    message= forms.CharField(widget=forms.Textarea
                             (attrs={'placeholder':'Enter Your Message'}))
    


