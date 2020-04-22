from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    mobile_number = forms.CharField(min_length=10,max_length=10)
    address = forms.CharField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class Id_SalaryForm(forms.Form):
    id = forms.IntegerField()
    new_salary = forms.IntegerField()

class Id_Form(forms.Form):
    id = forms.IntegerField()
    
class New_Employee(forms.Form):
    #create table employee(id int primary key, name varchar(200),position varchar(100) not null,mobile varchar(200),address varchar(1000),salary int not null, email varchar(1000));
    id = forms.IntegerField()
    name = forms.CharField(min_length=1)
    STATES = (
        ('', 'Choose...'),
        ('E1', 'Accounts Employee'),
        ('E2', 'Game Maker'),
        ('E3', 'Casino Dealer')
    )
    position = forms.ChoiceField(choices = STATES)
    mobile = forms.CharField(min_length=10,max_length=10)
    address = forms.CharField(min_length=1)
    salary = forms.IntegerField()
    email = forms.CharField()
    
    

