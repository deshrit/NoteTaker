from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import SignupForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

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


