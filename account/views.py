from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .forms import (RegisterForm, 
                    LoginForm,
                    PasswordChangeCustomForm, 
                    CustomPasswordResetForm, 
                    CustomSetPasswordForm)
from django.utils.encoding import force_str, force_bytes
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from multikart.settings import EMAIL_HOST_USER
from django.contrib.auth.views import (PasswordChangeView, 
                                        PasswordResetView, 
                                        PasswordResetConfirmView, 
                                        LoginView)
from django.views.generic import CreateView, TemplateView, ListView
from django.utils.http import urlsafe_base64_decode
from account.utils.tokens import account_activation_token
from django.contrib import messages
from .models import User
# from verify_email import verify_email

class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # email = form.instance.email
        # email_list = User.objects.values_list("email", flat=True)
        # if not email in email_list:
        #     if verify_email(email):
        form.instance.set_password(form.cleaned_data['password1'])
        form.instance.is_active = False
        form.instance.save()

        subject = 'Activate Your SuperB Account'
        current_site = get_current_site(self.request)
        message = render_to_string('email/confirmation_email.html', {
                'user': form.instance,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(form.instance.pk)),
                'token': account_activation_token.make_token(form.instance),
            })
        from_email = EMAIL_HOST_USER
        to_email = self.request.POST['email']
        send_mail(
            subject,
            message,
            from_email,
            [to_email, ]
        )
        messages.success(self.request, ('Please confirm your email to complete registration.'))
        return redirect('login')
    # messages.error(self.request, ('Please write a real email to complete registration.'))
    # return redirect('register')
    # else: 
    # messages.error(self.request, ('You have been registered with this email! Please write a different email to complete registration!'))
    # return redirect('register')

class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    authentication_form = LoginForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super(LoginView, self).dispatch(request, *args, **kwargs)

class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'email/password_message.html'
    form_class = CustomPasswordResetForm
    template_name = 'password/password_reset.html'
    success_url = reverse_lazy('password_reset_done')
    
    def get_success_url(self):
        messages.success(self.request, 'Your request to change your password has been registered. Please check your email.')
        return super(CustomPasswordResetView, self).get_success_url()

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password/password_reset_confirm.html'
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy('password_reset_complete')

    def get_success_url(self):
        messages.success(self.request, 'Your password has been successfully changed!')
        return super(CustomPasswordResetConfirmView, self).get_success_url()

class CustomPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeCustomForm
    template_name = 'change_password.html'
    success_url = reverse_lazy('change_password')

    def get_success_url(self):
        messages.success(self.request, 'Your password has been successfully changed!')
        return super(CustomPasswordChangeView, self).get_success_url()

class CustomResetEmailConfirmView(TemplateView):
    template_name   = "password/password_reset_done.html"

class CustomPasswordResetCompleteView(TemplateView):
    template_name   = "password/password_reset_complete.html"
    
def activate(request, uidb64, token):
    uid = force_str(urlsafe_base64_decode(uidb64))
    user = User.objects.filter(pk=uid, is_active=False).first()

    if user is not None and account_activation_token.check_token(user, token):
        messages.success(request, 'Your profile is activated')
        user.is_active = True
        user.save()
        return redirect('/login/')
    else:
        messages.error(request, 'Your session is expired')
        return redirect('/')
 
def profile(request):
    return render(request, 'profile.html')
    
def forget_pwd(request):
    return render(request, 'forget_pwd.html')