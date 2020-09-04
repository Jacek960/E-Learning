from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView
from django.views.generic.base import View

from accounts.forms import SignUpForm, UserUpdateForm


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserProfile(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(username=request.user)
        return render(request, 'accounts/user-profile.html', {'user': user})


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'accounts/user_profile_update_form.html'
    success_url = reverse_lazy('user_profile')

    def get_object(self, queryset=None):
        return self.request.user
