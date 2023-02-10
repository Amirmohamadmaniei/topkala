from datetime import timedelta
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from utils import create_send_otp
from .forms import UserLoginForm, UserRegisterForm, ChangePasswordForm, OTPForm, ForgetPasswordForm, VerifyPhoneForm, \
    SetNewPasswordForm
from .models import User, OTP
from .mixins import NotLoginRequiredMixin
from django.utils import timezone


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
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
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
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']

            create_send_otp(phone)

            request.session['phone'] = phone
            request.session['password'] = password
            return redirect('account:confirm')
        return render(request, self.template_name, {'form': form})


class ConfirmOTPView(NotLoginRequiredMixin, View):
    form_class = OTPForm
    template_name = 'account/confirm_otp.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            now = timezone.now()
            code = form.cleaned_data['code']
            phone = request.session['phone']
            password = request.session['password']

            try:
                otp = OTP.objects.get(code=code, phone=phone)

                if otp.created + timedelta(minutes=2) > now:

                    user = User.objects.create_user(phone=phone, password=password)
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    otp.delete()
                    return redirect('account:welcome')
                else:
                    form.add_error('code', 'کد تایید باطل شده است')
                    otp.delete()
            except:
                form.add_error('code', 'کد تایید اشتباه است')

        return render(request, self.template_name, {'form': form})


class SendOTP(NotLoginRequiredMixin, View):
    def get(self, request):
        phone = request.session['phone']
        create_send_otp(phone)
        return redirect('account:confirm')


class WelcomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'account/welcome.html')


class ChangePassword(LoginRequiredMixin, View):
    form_class = ChangePasswordForm
    template_name = 'account/change_password.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.get(pk=request.user.pk)
            if user.check_password(cd['old_password']):
                user.set_password(cd['password'])
                return redirect('profile:profile')
            else:
                form.add_error('old_password', 'رمز عبور اشتباه است')
        return render(request, self.template_name, {'form': form})


class ForgetPasswordView(NotLoginRequiredMixin, View):
    form_class = ForgetPasswordForm
    template_name = 'account/forget_password.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            request.session['phone'] = phone
            create_send_otp(phone)
            return redirect('account:verify_phone')
        return render(request, self.template_name, {'form': form})


class VerifyPhoneView(NotLoginRequiredMixin, View):
    form_class = VerifyPhoneForm
    template_name = 'account/verify_phone.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            now = timezone.now()
            code = form.cleaned_data['code']
            phone = request.session.get('phone')

            try:
                otp = OTP.objects.get(code=code, phone=phone)
                if otp.created + timedelta(minutes=2) > now:
                    request.session['is_valid'] = True
                    return redirect('account:set_password')
                else:
                    form.add_error('code', 'کد تایید باطل شده است')
                    otp.delete()
            except:
                form.add_error('code', 'کد تایید اشتباه است')

        return render(request, self.template_name, {'form': form})


class SetNewPasswordView(NotLoginRequiredMixin, View):
    form_class = SetNewPasswordForm
    template_name = 'account/set_new_password.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('is_valid'):
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            phone = request.session.get('phone')
            user = User.objects.get(phone=phone)
            if not user.check_password(password):
                user.set_password(password)
                user.save()
                messages.success(request, 'رمز عبور با موفقیت تغییر کرد', extra_tags='alert alert-success')
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('profile:profile')
            else:
                form.add_error(None, 'رمز تکراری است , رمز جدیدی وارد کنید')
        return render(request, self.template_name, {'form': form})
