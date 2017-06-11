#coding=utf-8
"""cnonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve
from django.views.generic import TemplateView
import xadmin
from users.views import IndexView

from users.views import LoginView,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView,LogOutView
from organization.views import OrgView
from cnonline.settings import MEDIA_ROOT



urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(),name="index"),
    url(r'^login/$', LoginView.as_view(),name="login"),
    url(r'^logout/$', LogOutView.as_view(),name="logout"),
    url(r'^register/$', RegisterView.as_view(),name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>\.*)/$', ActiveUserView.as_view(),name="ActiveUserView"),
    url(r'^forget/$', ForgetPwdView.as_view(),name="ForgetPwdView"),
    url(r'^reset/(?P<active_code>\.*)/$', ResetView.as_view(),name="ResetView"),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(),name="ModifyPwdView"),
    # 课程机构URL配置
    url(r'^org/', include('organization.urls',namespace="org")),
    # 课程相关URL配置
    url(r'^course/', include('courses.urls', namespace="course")),
    # 用户相关URL配置
    url(r'^users/', include('users.urls', namespace="users")),
    # 配置上传文件访问处理函数
    url(r'^media/(?P<path>.*)$', serve,{"document_root":MEDIA_ROOT}),
    # 富文本相关URL
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
    # url(r'^static/(?P<path>.*)$', serve,{"document_root":STATIC_ROOT}),
]
#全局404 500 页面配置
# (放ViewS的路径)
handler404='users.views.page_not_found'
handler500='users.views.page_error'