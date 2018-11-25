from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from scripts.models import newTeamcreation,attendance,allMembers

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

    team_member = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'size':'10'}),
                                            queryset=User.objects.all())

    class Meta:
        model = newTeamcreation
        
        # team_member = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'size':'10'}),
        #                                         queryset=User.objects.all())

    # def __init__(self, *args, **kwargs):
    #     super(PostteamForm,self).__init__(*args,**kwargs)
    #     self.fields['team_member']=forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'size':'10'}),
    #                                                  queryset=User.objects.all(),required=True)
    #

        fields = {
            'team_name': forms.TextInput(attrs={'placeholder': 'What\'s your Team name?'}),
            'team_description': forms.TextInput(attrs={'placeholder': 'Team description'}),
            'team_member' : forms.ModelMultipleChoiceField(widget=forms.SelectMultiple(attrs={'size':'10'}),
                                                    queryset=User.objects.all())

        }
    def clean_teamcreated_by(self):
        if not self.cleaned_data['team_created_by']:
            return User()
        return self.cleaned_data['team_created_by']

class attendanceForm(forms.ModelForm):
    code = forms.CharField(label='Your code', required=True)

    class Meta:
        model = attendance
        fields = ('user','code','ip_address','att_date')
