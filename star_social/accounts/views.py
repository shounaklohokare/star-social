from django.shortcuts import render
from django.core.unresolvers import reverse_lazy
from django.views.generic import CreateView
# Create your views here.

from . import forms


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    # will redirect to the url after successful sign up
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
