from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    nickname = forms.CharField(max_length=30, required=True, label=_('닉네임'))

    class Meta:
        model = CustomUser
        fields = ('username', 'nickname', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = _('아이디')
        self.fields['username'].help_text = None
        self.fields['email'].label = _('이메일')
        self.fields['email'].help_text = None
        self.fields['password1'].label = _('비밀번호')
        self.fields['password1'].help_text = None
        self.fields['password2'].label = _('비밀번호 확인')
        self.fields['password2'].help_text = None

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError(_('이미 사용 중인 아이디입니다.'))
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError(_('이미 사용 중인 이메일입니다.'))
        return email

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if CustomUser.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError(_('이미 사용 중인 닉네임입니다.'))
        return nickname

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(_('비밀번호가 일치하지 않습니다.'))
            if len(password1) < 8:
                raise forms.ValidationError(_('비밀번호가 너무 짧습니다. 8자 이상이어야 합니다.'))
            if password1.isnumeric():
                raise forms.ValidationError(_('비밀번호는 숫자로만 이루어질 수 없습니다.'))
            common_passwords = ['password', '12345678', 'qwerty', 'abc123']
            if password1.lower() in common_passwords:
                raise forms.ValidationError(_('비밀번호가 너무 흔합니다.'))
        return password2
