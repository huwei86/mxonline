#coding=utf-8
__auth__ = 'huwei'
__date__ = '2017/4/12 15:02'
import xadmin
from .models import Course,Lesson,Video,CourseResource,BannerCourse
from organization.models import CourseOrg
# 章节与课程嵌套 inlines模式
class LessonInline(object):
    model = Lesson
    extra=0


class CourseAdmin(object):
    # 查看
    list_display=['name','desc','detail','degree','learn_time','students','fav_nums','image','click_num','add_time','get_zj_nums']
    # 查找
    search_fields=['name','desc','detail','degree','learn_time','students','fav_nums','image','click_num']
    # 过滤
    list_filter=['name','desc','detail','degree','learn_time','students','fav_nums','image','click_num','add_time']
    # 根据点击数排列
    ordering=['-click_num']
    # 只读
    readonly_fields=['click_num','fav_nums']
    # 在列表页直接修改
    list_editable=['degree','desc']
    inlines = [LessonInline]
    # 自动刷新页面 3，5表示秒数
    refresh_times = [3,5]
    # 指明课程中detail字段 用富文本编辑
    style_fields={"detail":"ueditor"}
    import_excel = True

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj=self.new_obj
        obj.save()
        if obj.CourseOrg is not None:
            course_org=obj.CourseOrg
            course_org.course_nums=Course.objects.filter(CourseOrg=course_org).count()
            course_org.save()
    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(CourseAdmin, self).post(request, args, kwargs)

class BannerCourseAdmin(object):
    # 查看
    list_display=['name','desc','detail','degree','learn_time','students','fav_nums','image','click_num','add_time']
    # 查找
    search_fields=['name','desc','detail','degree','learn_time','students','fav_nums','image','click_num']
    # 过滤
    list_filter=['name','desc','detail','degree','learn_time','students','fav_nums','image','click_num','add_time']
    # 根据点击数排列
    ordering=['-click_num']
    # 只读
    readonly_fields=['click_num','fav_nums']
    inlines = [LessonInline]


    def queryset(self):
        qs=super(BannerCourseAdmin,self).queryset()
        qs=qs.filter(is_banner=True)
        return qs


class LessonAdmin(object):
    list_display = ['course', 'name','add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name','add_time']



class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'add_time']





class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download','add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course__name', 'name', 'download','add_time']









xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(BannerCourse,BannerCourseAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
