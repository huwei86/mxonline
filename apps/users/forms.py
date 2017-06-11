#coding=utf-8
__auth__ = 'huwei'
__date__ = '2017/4/15 11:43'
from django import forms
from captcha.fields import CaptchaField
from .models import UserProfile


class LoginForm(forms.Form):
    username=forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)



class RegisterForm(forms.Form):
    email=forms.EmailField(required=True)
    password=forms.CharField(required=True,min_length=5)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})




class ForgetForm(forms.Form):
    email=forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})

class ModifyPwdForm(forms.Form):
    password1=forms.CharField(required=True,min_length=5)
    password2 = forms.CharField(required=True,min_length=5)


class UpLoadImageForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['image']



class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['nick_name','gender','birday','address','mobile']