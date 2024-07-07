from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_protect
# from apps.users.models import Account

from apps.doctors.models import Doctor
from apps.users.forms import UserCreationForm, UserUpdateForm, RegisterForm, UserLoginForm
from django.views.generic import DeleteView, TemplateView
from django.contrib.auth.models import User
from django.views import View


User = get_user_model()


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctor.objects.all()

        return context


class UserCreateView(generic.CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'users/account.html'
    success_url = '/'


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


# class RegisterView(View):
#     def get(self, request):
#         form = UserCreationForm()
#         return render(request, 'login-form/register.html', {'form': form})

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect(reverse_lazy('home'))
#         return render(request, 'login-form/register.html', {'form': form})


# class LoginView(View):
#     def get(self, request):
#         form = UserLoginForm()
#         return render(request, 'login-form/register.html', {'form': form})

#     def post(self, request):
#         form = UserLoginForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('/')
#         return render(request, 'login-form/register.html', {'form': form})

# @login_required
# def logout_view(request):
#     logout(request)
#     return redirect('home')


# Ваш файл views.py
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegistrationForm



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



# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             is_admin = form.cleaned_data.get('is_admin')
 
            
#             if is_admin:
#                 if user.is_staff: 
#                     user = User.objects.create_superuser(username=username, password=password)
#                 else:
#                     return redirect('registration_failed')
#             else:
#                 user = User.objects.create_user(username=username, password=password)

#             return redirect('index.html')

#             # Автоматически входим пользователя после регистрации
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('index.html')  # Замените на ваше имя URL-а успеха

#     else:
#         form = UserRegistrationForm()

#     return render(request, 'login-form/register.html', {'form': form})


# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')  # Исправлено на ваше имя URL-а успеха
#     else:
#         form = UserRegistrationForm()

#     return render(request, 'login-form/register.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            is_admin = form.cleaned_data['is_admin']  # Если требуется

            # Создание пользователя
            user = CustomUser.objects.create_user(username=username, email=email, password=password)

            # Автоматически входим пользователя после регистрации
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index.html')  # Замените на ваше имя URL-а успеха

    else:
        form = UserRegistrationForm()

    return render(request, 'login-form/register.html', {'form': form})