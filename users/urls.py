from django.urls import path
from django.views.generic import TemplateView

from users import views

urlpatterns = [
    path(
        route='login',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='signup',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='me/profile',
        view=views.UpdateProfileView.as_view(),
        name='update'
    ),
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
]