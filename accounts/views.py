from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomLoginForm, CustomSignUpForm

from django.contrib import messages

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomSignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'registro exitoso')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'algo salio mal')
        return super().form_invalid(form)

class LoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'registration/login.html'

class LogoutView(LogoutView):
    template_name = 'registration/logout.html'
