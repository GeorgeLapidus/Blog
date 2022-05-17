from django.urls import path

from account.views import UserLoginView, UserLogoutView, profile, RegisterUser, RegisterDoneView, ChangeUserDataView, \
    ChangeUserPasswordView


app_name = 'account'

urlpatterns = [

    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('password/change/', ChangeUserPasswordView.as_view(), name='change_user_password'),
    path('profile/change/', ChangeUserDataView.as_view(), name='change_user_data'),
    path('profile/', profile, name='profile'),
    path('register/done/', RegisterUser.as_view(), name='register'),
    path('register/', RegisterDoneView.as_view(), name='register_done'),

]