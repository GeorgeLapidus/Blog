from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from account.models import BlogUser

from account.forms import RegistrationUserForm, ChangeUserDataForm


class UserLoginView(LoginView):
    """Класс авторизации пользователя на сайте"""
    template_name = "login.html"


class UserLogoutView(LogoutView):
    """Класс для выхода пользователя с аккаунта"""
    template_name = "logout.html"


@login_required
def profile(request):
    """Функция для отображения профиля авторизованного пользователя"""
    return render(request, 'profile.html')


class RegisterUser(CreateView):
    """Класс, регистрирующий пользователя на сайте"""

    model = BlogUser
    form_class = RegistrationUserForm
    template_name = "register.html"
    success_url = reverse_lazy('main:start_page')


class RegisterDoneView(TemplateView):
    """Класс, выводящий сообщение при успешной регистрации пользователя на сайте"""
    template_name = 'register_done.html'


class ChangeUserDataView(UpdateView, LoginRequiredMixin):
    """Класс для изменения данных авторизованного пользователя"""
    model = BlogUser
    template_name = "change_user_data.html"
    form_class = ChangeUserDataForm
    success_url = reverse_lazy("account:profile")

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class ChangeUserPasswordView(PasswordChangeView, LoginRequiredMixin):
    """Класс для изменения пароля пользователя"""
    model = BlogUser
    template_name = "change_user_password.html"
    success_url = reverse_lazy("account:profile")
