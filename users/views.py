from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from .forms import (
    SignupForm, 
    LoginForm, 
    UserUpdateForm, 
    ProfileUpdateForm,
    PassResetForm,
    PassNewForm,
)
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from note.models import Note
from django.contrib.auth.models import User


class UserSignupView(View):
    form_class = SignupForm
    template_name = "users/signup.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('note:index')
        
        form = self.form_class() 
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")
        context = {
            "form": form
        }
        return render(request, self.template_name, context)
    

class UserLoginView(LoginView):
    template_name = "users/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True
    next_page = "/"

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        response =  super().post(request, *args, **kwargs)
        # changing guest to user and keeping notes
        guest = request.COOKIES.get('guest')
        if guest:
            if request.user.is_authenticated:
                Note.objects.filter(user__username=guest).update(user=request.user)
                User.objects.filter(username=guest).delete()
                response.delete_cookie('guest')
        return response


class ProfileView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')
    template_name = "users/profile.html"

    def get(self, request, *args, **kwargs):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(data=request.POST,instance=request.user)
        p_form = ProfileUpdateForm(
            data=request.POST,
            files=request.FILES,
            instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('users:profile')
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, self.template_name, context)


class UserLogoutView(LogoutView):
    next_page = "/login/"


class PassResetView(PasswordResetView):
    template_name = "users/password_reset.html"
    form_class = PassResetForm
    success_url = reverse_lazy("users:password_reset_done")
    email_template_name = "users/email_template.html"

class PassResetDoneView(PasswordResetDoneView):
    template_name = "users/password_reset_done.html"

class PassResetConfirmView(PasswordResetConfirmView):
    template_name = "users/password_reset_confirm.html"
    success_url = reverse_lazy("users:password_reset_complete")
    form_class = PassNewForm

class PassResetCompleteView(PasswordResetCompleteView):
    template_name = "users/password_reset_complete.html"