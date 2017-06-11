#coding=utf-8
__auth__ = 'huwei'
__date__ = '2017/4/19 9:59'
from django.conf.urls import url
from .views import CourseListView,CourseDetailView,CourseInfoView,CommentsView,AddComentsView


urlpatterns = [
    # 课程列表页
    url(r'^list/', CourseListView.as_view(),name="course_list"),
    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(),name="course_detail"),
    #课程章节信息
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(),name="course_info"),
    #课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(),name="course_comment"),
    # 添加评论
    url(r'^add_comment/$', AddComentsView.as_view(),name="add_comment"),



]
