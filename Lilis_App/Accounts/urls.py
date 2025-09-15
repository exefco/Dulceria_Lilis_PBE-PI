from django.urls import path
from .views import Login,Registrarse, Logout, Password_reset

urlpatterns = [
    path('login/', Login.as_view(template_name='accounts/login.html'), name='login'),
    path('registrarse/', Registrarse.as_view(template_name="accounts/register.html"), name='registrarse'),
    path('logout/', Logout, name='logout'),
    path('password_reset/', Password_reset.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
]