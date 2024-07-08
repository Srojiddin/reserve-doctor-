from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_protect
# from apps.users.models import Account
from django.contrib import messages


from apps.doctors.models import Doctor
from apps.users.forms import UserCreationForm, UserUpdateForm, RegisterForm, UserLoginForm
from django.views.generic import DeleteView, TemplateView
from django.views import View


User = get_user_model()


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctor.objects.all()

        return context

    

class SuperuserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

class UserCreateView(SuperuserRequiredMixin, LoginRequiredMixin, generic.CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'login-form/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usernames'] = User.objects.values_list('username', flat=True).distinct()
        context['emails'] = User.objects.values_list('email', flat=True).distinct()
        return context

class UserDetailView(generic.DetailView):
    model = User
    template_name = 'users/users_detail.html'
    context_object_name = 'user'


class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/users_update.html'
    context_object_name = 'user'
    success_url = '/profile/'


class UserProfileView(generic.DetailView):
    model = User
    template_name = 'users/user_profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/user_delete.html'
    context_object_name = 'user'
    success_url = '/index.html'


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')


# # Ваш файл views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from .forms import UserRegistrationForm



# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             is_admin = form.cleaned_data['is_admin']

#             if is_admin:
#                 if user.is_staff: 
#                     user = User.objects.create_superuser(username=username, password=password)
#                 else:
#                     return redirect('registration_failed')
#             else:
#                 user = User.objects.create_user(username=username, password=password)

#             return redirect('registration_success')

#     else:
#         form = UserRegistrationForm()

#     return render(request, 'login-form/register.html', {'form': form})

