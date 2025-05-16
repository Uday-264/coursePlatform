from cloudinary import CloudinaryImage
from django.contrib import admin
from django.utils.html import format_html
from .models import Course,Lesson
import helpers 
# Register your models here.

class LessonInline(admin.StackedInline):
    model=Lesson
    readonly_fields=['public_id','updated','display_image','display_video']
    extra=0
    def display_image(self,obj,*args,**kwargs):
        url=helpers.get_cloudinary_image_object(obj,field_name='thumbnail',width=200)
        return format_html(f"<img src='{url}'/>")   
    display_image.short_decsription='Current Image'
    def display_video(self,obj,*args,**kwargs):
        video_embedded=helpers.get_cloudinary_video_object(obj,field_name='video',width=600,as_html=True)
        return video_embedded   
    display_video.short_decsription='Current video'
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines=[LessonInline]
    list_display=['title','status','access']
    list_filter=['title','access']
    fields=['public_id','title','description','status','image','access','display_image']
    readonly_fields=['public_id','display_image']

    def display_image(self,obj,*args,**kwargs):
        url=obj.image_admin_url
        # cloudinary_id=str(obj.image)
        # cloudinary_image= CloudinaryImage(cloudinary_id).image(width=500)
        return format_html(f"<img src='{url}'/>")
        
    display_image.short_decsription='Current Image'
# admin.site.register(Course,CourseAdmin)