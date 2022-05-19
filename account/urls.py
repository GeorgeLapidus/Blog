from django.urls import path

from account.views import UserLoginView, UserLogoutView, profile, RegisterUser, RegisterDoneView, ChangeUserDataView, \
    ChangeUserPasswordView

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

from django.urls import reverse_lazy

app_name = 'account'

urlpatterns = [

    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('password/change/', ChangeUserPasswordView.as_view(), name='change_user_password'),
    path('profile/change/', ChangeUserDataView.as_view(), name='change_user_data'),
    path('profile/', profile, name='profile'),
    path('register/done/', RegisterUser.as_view(), name='register'),
    path('register/', RegisterDoneView.as_view(), name='register_done'),
    path('password/reset_done/', PasswordResetDoneView.as_view(template_name='email_sent.html'),
         name='password_reset_done'),
    path('password_reset/',
         PasswordResetView.as_view(template_name='reset_password.html', subject_template_name='reset_subject.txt',
                                   email_template_name='reset_email.txt',
                                   success_url=reverse_lazy("account:password_reset_done")), name='reset_password'),

    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='confirm_password.html',
                                                                     success_url=reverse_lazy(
                                                                         "account:password_reset_complete")),
         name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='password_confirmed.html'),
         name='password_reset_complete'),

]
