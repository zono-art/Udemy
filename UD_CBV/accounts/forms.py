from django import forms
from .models import Users
from django.contrib.auth.password_validation import validate_password

class RegistForm(forms.ModelForm):
    username = forms.CharField(label="名前")
    age = forms.IntegerField(label="年齢")
    email = forms.EmailField(label="メールアドレス")
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput())
    class Meta:
        model = Users
        fields = ["username", "age", "email", "password"]
    #パスワードを暗号化
    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data["password"], user)
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user

