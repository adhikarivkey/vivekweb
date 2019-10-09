from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from .forms import UserForm
# from django.contrib.auth.views import PasswordResetView
from django.contrib import messages
# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class SignUpPage(CreateView):
	form_class = UserForm
	template_name = 'signup.html'
	success_url = reverse_lazy('login')

# class UserPasswordResetView(PasswordResetView):
#     template_name = 'password_reset_form.html'
#     success_url = reverse_lazy('custom_auth:password_reset_done')
#     subject_template_name = 'password_reset_subject.txt'
#     # email_template_name = 'password_reset_email.html'