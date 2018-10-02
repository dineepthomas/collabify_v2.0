from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.http import JsonResponse
from django.views import generic
from django.shortcuts import render,render_to_response, HttpResponse, redirect
from django_fine_uploader.fineuploader import SimpleFineUploader
from django_fine_uploader.forms import FineUploaderUploadForm
from django_fine_uploader.views import FineUploaderView
import subprocess,os,json
from django.http import HttpResponse,HttpResponseRedirect
from subprocess import Popen, PIPE
from django.template import Context, loader,RequestContext
from django.urls import reverse
from django.views.generic import FormView, DetailView, ListView
from django.contrib.auth.models import User
import codecs

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Media root
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# Media URL
MEDIA_URL = '/media/'
print(MEDIA_ROOT)
from . forms import(
    registrationForm, editProfileform
)

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

from django.contrib.auth import update_session_auth_hash # to make sure after password reset user name comes instead of
                                        # anonymous username. so this basically saves our session!!

from django.contrib.auth.decorators import login_required # to prevent sites to be accessed based on url. only if logged
                                        # in then show the page or else don't.


def home(request):
    return render(request,'accounts/HomePage.html',{})

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        u = User.objects.create_user(username, email, password, first_name=fname, last_name=lname)
        u.save()
        return HttpResponse("Registration complete! Please head over to the <a href='/login/'>login page</a> to start using the website.")

    return render(request, "accounts/new_register.html", {})

def view_profile(request):

    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):

    if request.method == 'POST':
        form = editProfileform(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile/')
    else:
        form = editProfileform(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile/')
        else:
            return redirect('/account/change_password/')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
