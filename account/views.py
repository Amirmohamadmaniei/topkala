from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserLoginForm, UserRegisterForm
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
