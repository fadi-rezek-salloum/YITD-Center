from django.views import generic
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import get_language, gettext_lazy as _

from .models import User
from .forms import UserCreationForm, UserChangeForm

class RegisterUserView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "accounts/register.html"
    success_url = f"/{get_language()}/account/login"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')

        return super().dispatch(request, *args, **kwargs)


class LoginUserView(LoginView):
    template_name = "accounts/login.html"
    
    def post(self, request, *args, **kwargs):
        post = super().post(request, *args, **kwargs)

        if post.status_code == 302:
            return HttpResponseRedirect(f'/{get_language()}/')

        return post


class LogoutUserView(LoginRequiredMixin, LogoutView):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(f'/{get_language()}/')


class UpdateUserView(LoginRequiredMixin, generic.UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = "accounts/update_profile.html"

    def get(self, request, *args, **kwargs):

        if not str(request.user.pk) == kwargs['pk']:
            return HttpResponseRedirect('/')

        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):

        if self.form_class.is_valid:
            messages.success(request, _("Your profile was update successfully!"))
        
        self.success_url = f"/{get_language()}/account/profile/{kwargs['pk']}/"
        return super().post(request, *args, **kwargs)