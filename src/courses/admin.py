from cloudinary import CloudinaryImage
from django.contrib import admin
from django.utils.html import format_html
from .models import Course
# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=['title','status','access']
    list_filter=['title','access']
    fields=['title','description','status','image','access','display_image']
    readonly_fields=['display_image']

    def display_image(self,obj,*args,**kwargs):
        url=obj.image_admin_url
        # cloudinary_id=str(obj.image)
        # cloudinary_image= CloudinaryImage(cloudinary_id).image(width=500)
        return format_html(f"<img src='{url}'/>")
        
    display_image.short_decsription='Current Image'
# admin.site.register(Course,CourseAdmin)