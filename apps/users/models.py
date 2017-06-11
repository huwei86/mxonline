#coding=utf-8
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# 采用继承的方式扩展用户信息
class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=50,verbose_name=u"昵称")
    birday=models.DateField(max_length=50,null=True,blank=True,verbose_name=u"生日")
    gender=models.CharField(choices=(("male",u"男"),("female",u"女")),default=u"female",max_length=10)
    address=models.CharField(max_length=100,default=u"")
    mobile=models.CharField(max_length=11,null=True,blank=True)
    image=models.ImageField(upload_to="image/%y/%m",default=u"image/default.png",max_length=100)

    class Mate:
        verbose_name=u"用户信息"
        verbose_name_plural=verbose_name
        ordering=["-id"]
    def __unicode__(self):
         return self.username
    def unread_message_nums(self):
        # 获取用户未读消息的数量
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id,has_read=False).count()






class EmailVerifyRecord(models.Model):
    code=models.CharField(max_length=20,verbose_name=u"验证码")
    email=models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_type=models.CharField(verbose_name=u"发送类型",choices=(("register",u"注册"),("forget",u"忘记密码"),("update_email",u"修改邮箱")),max_length=50)
    send_time=models.DateTimeField(verbose_name=u"发送时间",default=datetime.now)


    class Meta:
        verbose_name=u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code,self.email)





class Banner(models.Model):
    title=models.CharField(max_length=100,verbose_name=u"标题")
    image=models.ImageField(upload_to="banner/%y/%m",verbose_name=u"轮播图")
    url=models.URLField(max_length=200,verbose_name=u"访问地址")
    index=models.IntegerField(default=100,verbose_name=u"顺序")
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Mate:
        verbose_name=u"轮播图"
        verbose_name_plural=verbose_name




