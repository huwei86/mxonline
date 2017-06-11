#coding=utf-8
from __future__ import unicode_literals
from datetime import datetime
from organization.models import CourseOrg
from DjangoUeditor.models import UEditorField

from django.db import models
from organization.models import Teacher

# Create your models here.


class Course(models.Model):
    CourseOrg=models.ForeignKey(CourseOrg,verbose_name=u"课程机构",null=True,blank=True)
    name=models.CharField(max_length=50,verbose_name=u"课程名称")
    desc=models.CharField(max_length=300,verbose_name=u"课程描述")
    detail=UEditorField(verbose_name=u"课程详情",width=600, height=300, imagePath="courses/ueditor/", filePath="courses/ueditor/",default='' )
    is_banner=models.BooleanField(default=False,verbose_name=u"是否轮播")
    degree=models.CharField(choices=(("cj",u"初级"),("zj", u"中级"),("gj", u"高级")),max_length=2,verbose_name=u"难度")
    learn_time=models.IntegerField(default=0,verbose_name=u"学习时长(分钟)")
    students=models.IntegerField(default=0,verbose_name=u"学习人数")
    fav_nums=models.IntegerField(default=0,verbose_name=u"收藏人数")
    teacher=models.ForeignKey(Teacher,verbose_name=u"讲师",default='')
    image=models.ImageField(upload_to="courses/%y/%m",verbose_name=u"封面图", max_length=100)
    category=models.CharField(verbose_name=u"课程类别",max_length=300, default='')
    click_num=models.IntegerField(default=0,verbose_name=u"点击数")
    tag=models.CharField(verbose_name=u"课程标签",default='',max_length=20)
    add_time=models.DateTimeField(default=datetime.now,verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


    def get_zj_nums(self):
        # 获取课程章节数
        return self.lesson_set.all().count()
    get_zj_nums.short_description="章节数"




    def get_course_lesson(self):
        # 获取课程所有章节
        return self.lesson_set.all()

    def get_learn_users(self):
        # 获取课程用户（取3个用户显示）
        return self.usercourse_set.all()[:3]






class Lesson(models.Model):
    course=models.ForeignKey(Course,verbose_name=u"课程")
    name=models.CharField(max_length=100,verbose_name=u"章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_lesson_video(self):
        # 获取章节视频
        return self.video_set.all()



class Video(models.Model):
    lesson=models.ForeignKey(Lesson,verbose_name=u"章节")
    name=models.CharField(max_length=100,verbose_name=u"视频名")
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时长(分钟)")
    url=models.CharField(verbose_name=u"访问地址",default='',max_length=200)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name




class CourseResource(models.Model):
    course=models.ForeignKey(Course,verbose_name=u"课程")
    name=models.CharField(max_length=100,verbose_name=u"名称")
    download=models.FileField(upload_to="course/resource/%y/%m",verbose_name=u"资源文件",max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name


class BannerCourse(Course):
    class Meta:
        verbose_name=u"轮播课程"
        verbose_name_plural=verbose_name
        # 不会在生成一张表 但是具有COURSE的功能
        proxy=True
