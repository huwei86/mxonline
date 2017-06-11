#coding=utf-8
__auth__ = 'huwei'
__date__ = '2017/4/12 14:12'

import xadmin
from xadmin import views
from .models import EmailVerifyRecord,Banner,UserProfile
from xadmin.plugins.auth import UserAdmin
# from django.contrib.auth.models import User


class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class GlobalSettings(object):
    site_title="菜鸟后台管理系统"
    site_footer="菜鸟在线网"
    menu_style="accordion"



class EmailVerifyRecordAdmin(object):
    list_display=['code','email','send_type','send_time']
    search_fields=['code','email','send_type']
    list_filter=['code','email','send_type','send_time']
    model_icon = 'fa fa-group'



class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index','add_time']


class UserProfileAdmin(UserAdmin):
    pass

# xadmin.site.unregister(User)
xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
# xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)



