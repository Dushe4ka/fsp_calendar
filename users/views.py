import secrets

from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView, DetailView
from config import settings

from users.forms import UserRegisterForm, UserUpdateForm, UserProfileForm
from users.models import User


class UserDetailView(DetailView):
    model = User
    form_class = UserProfileForm
    template_name = 'user_detail.html'


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Для подтверждения почты перейдите по ссылке {url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user_update.html'
    success_url = reverse_lazy('mycalendar:list')


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class GeneratePasswordView(PasswordResetView):
    form_class = PasswordResetForm
    template_name = 'users/generate.html'

    def form_valid(self, form):
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            if user:
                password = User.objects.make_random_password(12)
                user.set_password(password)
                user.save()
                send_mail(
                    'Смена пароля Liliya',
                    f'Ваш новый пароль: {password}',
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    )
            return redirect(reverse("users:login"))


class ContactsTemplateView(TemplateView):
    template_name = 'contacts.html'

