from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    age = forms.IntegerField()
    favorite_sport = forms.ChoiceField(choices=[
        ('cricket', 'Cricket'),
        ('football', 'Football'),
        ('baseball', 'Baseball'),
        ('tennis', 'Tennis'),
        ('golf', 'Golf'),
        ('badminton', 'Badminton'),
        ('kabaddi', 'Kabaddi'),
        ('boxing', 'Boxing'),
        ('athletics', 'Athletics'),
        ('chess', 'Chess'),
        ('swimming', 'Swimming'),
        ('shooting', 'Shooting'),
        ('wrestling', 'Wrestling'),
        ('tabletennis', 'Table Tennis'),
    ])

    class Meta:
        model = User
        fields = ["username", "email", "age", "password1", "password2", "favorite_sport"]
