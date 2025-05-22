from django.http import Http404,JsonResponse
from django.shortcuts import render,redirect
import helpers
from . import services
# Create your views here.
def course_list_view(request):
    query_set=services.get_public_courses()
    context={
        "object_list":query_set
    }
    template_name="courses/list.html"
    if request.htmx:
        template_name="courses/snippets/list-display.html"
        context['query_set']=query_set[:3]
    # return JsonResponse({"data":[x.path for x in query_set]})
    return render(request,template_name,context)

def course_detail_view(request,course_id=None,*args, **kwargs):
    course_obj=services.get_course_detail(course_id=course_id)
    if course_obj is None:
        raise Http404
    lesson_query_set=services.get_course_lessons(course_obj)
    context={
        "object":course_obj,
        "lesson_query_set":lesson_query_set
    }
    # return JsonResponse({"data":course_obj.id,"lesson_ids":[x.path for x in lessson_query_set]})
    return render(request,"courses/details.html",context)

def lesson_detail_view(request,course_id=None,lesson_id=None,*args, **kwargs):
    lesson_obj=services.get_lessson_detail(course_id=course_id,lesson_id=lesson_id)
    if lesson_obj is None:
        raise Http404
     
    # return JsonResponse({"data":lesson_obj.id})

    email_id_exists=request.session.get('email_id')
    if lesson_obj.requires_email and not email_id_exists:
        request.session['next_url']=request.path
        return render(request,'courses/email-required.html',{})
    template_name="courses/lesson-comming-soon.html"
    context={
        "object":lesson_obj
    }
    if not lesson_obj.is_comming_soon and lesson_obj.has_video:
        template_name="courses/lesson.html"
        video_embedded=helpers.get_cloudinary_video_object(lesson_obj,field_name='video',width=1250,as_html=True)
        context['video_embed']=video_embedded
    return render(request,template_name,context)

