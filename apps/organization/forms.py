#coding=utf-8
__auth__ = 'huwei'
__date__ = '2017/4/17 17:05'

from django import forms
from operation.models import UserAsk
import re

# class UserAskForm(forms.Form):
#     name=forms.CharField(required=True,min_length=2,max_length=20)
#     phone=forms.CharField(required=True,min_length=11,max_length=11)
#     course_name=forms.CharField(required=True,max_length=5,min_length=5)

class UserAskForm(forms.ModelForm):
    class Meta:
        model=UserAsk
        fields=['name','mobile','course_name']
    def clean_mobile(self):
        # 验证手机号码合法
        mobile=self.cleaned_data['mobile']
        REGEX_MOBILE="^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        P=re.compile(REGEX_MOBILE)
        if P.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法",code="mobile_invalid")