from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserLoginForm, UserRegisterForm, ChangePasswordForm
from .models import User
from .mixins import NotLoginRequiredMixin


class LoginView(NotLoginRequiredMixin, View):
    form_class = UserLoginForm
    template_name = 'account/login.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home:home')
            form.add_error(None, 'نام کاربری یا کلمه عبور صحیح نمی باشد')
        return render(request, self.template_name, {'form': form})


class LogoutView(LoginRequiredMixin, View):
    login_url = 'account:login'

    def get(self, request):
        logout(request)
        return redirect('home:home')


class RegisterView(NotLoginRequiredMixin, View):
    form_class = UserRegisterForm
    template_name = 'account/register.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(phone=cd['phone'], password=cd['password'])
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('account:welcome')
        return render(request, self.template_name, {'form': form})


class WelcomeView(NotLoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'account/welcome.html')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'account/profile.html')


class ChangePassword(LoginRequiredMixin, View):
    form_class = ChangePasswordForm
    template_name = 'account/change_password.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            print('ok')
            cd = form.cleaned_data
            user = User.objects.get(pk=request.user.pk)
            if user.check_password(cd['old_password']):
                user.set_password(cd['password'])
                return redirect('account:profile')
            else:
                form.add_error('old_password', 'رمز عبور اشتباه است')
        print('nok')
        return render(request, self.template_name, {'form': form})