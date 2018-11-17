from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect,render_to_response
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import update_session_auth_hash # to make sure after password reset user name comes instead of
                                        # anonymous username. so this basically saves our session!!
from django.contrib.auth.decorators import login_required # to prevent sites to be accessed based on url. only if logged
                                        # in then show the page or else don't.
from scripts.forms import SignUpForm,PostteamForm
from scripts.models import newTeam
from scripts.tokens import account_activation_token
from django.contrib import messages
from django.views.generic import TemplateView,FormView
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def team(request):
    return render(request, 'team_creation.html')


class test1(TemplateView):
    print("test1 called")
    template_name = 'post_team_info.html'

    def get(self,request):
        print("test1 get called")
        form = PostteamForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        print("test1 post called")
        form = PostteamForm(request.POST)
        args ={}
        if form.is_valid():
            print("test1 form valid called")
            text = form.cleaned_data['team_name']
            team_des = form.cleaned_data['team_description']
            team_list = form.cleaned_data['team_member']
            print(text)
            print(team_des)
            print(team_list)
            args = {'text':text,'team_des':team_des,'team_list':team_list}
            form = PostteamForm()

        return render(request,'team_info_display.html',args )




def attendance(request):
    return render(request, 'attendance_QR_Code.html')

def board(request):
    return render(request, 'board.html')

@login_required

def dashboard(request):
    form = UserCreationForm()
    c = {'form': form}
    return render_to_response("dashboard_2.html", {'name': request.user.username})

    # return render(request, 'dashboard.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': force_text(urlsafe_base64_encode(force_bytes(user.pk))),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('dashboard')
    else:
        return render(request, 'account_activation_invalid.html')

# @login_required
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('change_password')
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'change_password.html', {
#         'form': form
#     })
