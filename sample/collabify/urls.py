"""collabify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import TemplateView
from app import views
from django.contrib.auth.views import login,logout

from django.views.decorators.csrf import csrf_protect
admin.autodiscover()

urlpatterns = [
    url(r'^home/$',views.home, name ='home'),
    url(r'^$',login,{'template_name': 'accounts/login.html'}),
    url(r'^logout/$',logout,{'template_name': 'accounts/logout.html'}),
    url(r'^register/$',views.register,name ='register'),
    url(r'^profile/$',views.view_profile, name ='view_profile'),
    url(r'^profile/edit/$',views.edit_profile, name ='edit_profile'),
    url(r'^change_password/$',views.change_password, name ='change_password'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
