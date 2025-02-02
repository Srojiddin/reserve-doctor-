from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()



# class UserRegistrationForm(UserCreationForm):
#     is_admin = forms.BooleanField(label='Admin', required=False)

#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2', 'is_admin')

        

class UserRegistrationForm(UserCreationForm):
    is_admin = forms.BooleanField(label='Admin', required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_admin']  # Добавьте 'is_admin' если это нужно

    def clean_is_admin(self):
        is_admin = self.cleaned_data['is_admin']
        if is_admin and not self.instance.is_staff:
            raise forms.ValidationError("Only staff members can register as admins.")
        return is_admin



class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class UserCreationForm(UserCreationForm):
    class Meta(UserForm.Meta):
        fields = ['username', 'password1', 'password2']


class UserUpdateForm(UserChangeForm):
        class Meta:
            model = User
            fields = ['username', 'email', 'first_name', 'last_name']
            help_texts = {
                'username': 'Обязательно. 150 символов или меньше. Только буквы, цифры и @/./+/-/_.'
            }
            labels = {
                'username': 'Имя пользователя',
                'email': 'Адрес электронной почты',
                'first_name': 'Имя',
                'last_name': 'Фамилия'
            }


class UserDetailForm(forms.ModelForm):
    class Meta(UserForm.Meta):
        fields = ['username', 'email', 'first_name', 'last_name']


class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

