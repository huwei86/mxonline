#coding=utf-8
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .models import Course,CourseResource
from operation.models import UserFavorite,CourseComments,UserCourse
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
class CourseListView(View):
    def get(self,request):
        # 获取所有课程安最新排列
        all_courses=Course.objects.all().order_by("-add_time")
        # 获取所有的热门课程安点击数排列取3个
        hot_courses=Course.objects.all().order_by("-click_num")[:3]
        # 课程搜索
        search_keywords=request.GET.get('keywords','')
        if search_keywords:
            all_courses=all_courses.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords)|Q(detail__icontains=search_keywords))

        # 课程排序
        sort = request.GET.get("sort", "")
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            elif sort == "hot":
                all_courses = all_courses.order_by("-click_num")
        # 对课程列表分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        # Provide Paginator with the request object for complete querystring generatio
        p = Paginator(all_courses, 3, request=request)
        courses = p.page(page)
        return render(request,"course-list.html",{
            "all_courses":courses,
            "sort":sort,
            "hot_courses":hot_courses

        })


class CourseDetailView(View):
    # 课程详情页
    def get(self,request,course_id):
        course=Course.objects.get(id=int(course_id))
        # 增加课程点击数保成到数据库
        # course.click_num+=1
        # course.save()
        has_fav_course=False
        has_fav_org=False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user,fav_id=course_id,fav_type=1):
                has_fav_course=True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.CourseOrg.id, fav_type=2):
                has_fav_org=True
        tag=course.tag
        if tag:
            relate_courses=Course.objects.filter(tag=tag)[:1]
        else:
            relate_courses=[]
        return render(request,"course-detail.html",{
           "course":course,
           "relate_courses": relate_courses,
            "has_fav_course":has_fav_course,
            "has_fav_org":has_fav_org
        })





class CourseInfoView(View):
    # 课程章节信息
    def get(self,request,course_id):
        course=Course.objects.get(id=int(course_id))
        course.students += 1
        course.save()
        # 查询用户是否已经关联了该课程
        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()

        user_coursers=UserCourse.objects.filter(course=course)
        user_id=[ user_coursers.user_id for user_coursers in user_coursers]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_id)
        # 取出所有课程ID
        course_id=[ user_coursers.course_id for user_coursers in all_user_courses]
        # 获取学过该用户的其他的所有课程
        relate_courses=Course.objects.filter(id__in=course_id).order_by("-click_nums")[:3]
        all_resources=CourseResource.objects.filter(course=course)
        return render(request,"course-video.html",{
            "course":course,
            "course_resources":all_resources,
            "relate_courses":relate_courses
        })



class CommentsView(View):
    def get(self,request,course_id):
        course=Course.objects.get(id=int(course_id))
        all_resources = CourseResource.objects.filter(course=course)
        all_comments=CourseComments.objects.all()
        return render(request,"course-comment.html",{
            "course": course,
            "course_resources": all_resources,
            "all_comments":all_comments

        }
  )

class AddComentsView(View):
    # 用户添加课程评论
    def post(self,request):
        if not request.user.is_authenticated():
            # 判断用户登录状态
            return HttpResponse('{"status":"fail","msg":"用户未登录"}', content_type='application/json')
        course_id=request.POST.get("course_id",0)
        comments=request.POST.get("comments","")
        if course_id>0 and comments:
            course_comments=CourseComments()
            course=Course.objects.get(id=int(course_id))
            course_comments.course=course
            course_comments.comments=comments
            course_comments.user=request.user
            course_comments.save()
            return HttpResponse('{"status":"success","msg":"添加成功"}', content_type='application/json')

        else:
            return HttpResponse('{"status":"fail","msg":"添加出错"}', content_type='application/json')







