from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, GeneratePasswordView, ContactsTemplateView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('generate/', GeneratePasswordView.as_view(), name='generate'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
]
