from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from scripts.models import newTeam,attendance

CATEGORIES = (
    ('Alex', 'Alex'),
    ('John', 'John'),
    ('Peter', 'Peter'),
    ('Rambo', 'Rambo'),
    ('Jason', 'Jason'),
    ('Eric', 'Eric'),
    ('WLEE', 'Win Lee'),
    ('Tabusu', 'Tabusu'),
)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username','email', 'password1', 'password2', )

class PostteamForm(forms.ModelForm):

    team_member = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=CATEGORIES)

    class Meta:
        model = newTeam

        fields = {
            'team_name': forms.TextInput(attrs={'placeholder': 'What\'s your Team name?'}),
            'team_description': forms.TextInput(attrs={'placeholder': 'Team description'}),

        }

class attendanceForm(forms.ModelForm):
    code = forms.CharField(label='Your code', required=True)

    class Meta:
        model = attendance
        fields = ('user','code','ip_address','att_date')
