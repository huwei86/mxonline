#coding=utf-8
__auth__ = 'huwei'
__date__ = '2017/4/20 17:30'
from django.conf.urls import url,include
from .views import UserInfoView,UpLoadImageView,UpdatePwdView,SendEmailCodeView
from.views import UpdataEmailView,MyCourseView,MyFavOrgView,MyFavTeacherView,MyFavCourseView,MyMessageView


urlpatterns = [
    # 用户信息页
    url(r'^info/', UserInfoView.as_view(),name="user_info"),
    # 用户上传头像
    url(r'^image/upload/$', UpLoadImageView.as_view(),name="image_upload"),
    # 个人中心修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(),name="update_pwd"),
    #发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),
    # 修改邮箱
    url(r'^update_email/$', UpdataEmailView.as_view(), name="update_email"),
    # 我的课程
    url(r'^mycourse/$', MyCourseView.as_view(), name= "mycourse"),
    # 我收藏的课程机构
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name= "myfav_org"),
    # 我收藏的授课讲师
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name= "myfav_teacher"),
    # 我收藏的课程
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name= "myfav_course"),
    # 我的消息
    url(r'^mymessage/$', MyMessageView.as_view(), name="mymessage"),




]
