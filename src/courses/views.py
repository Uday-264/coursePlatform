from django.http import Http404,JsonResponse
from django.shortcuts import render
from . import services
# Create your views here.
def course_list_view(request):
    query_set=services.get_public_courses()
    print(query_set)
    return JsonResponse({"data":[x.path for x in query_set]})
    return render(request,"courses/list.html",{})

def course_detail_view(request,course_id=None,*args, **kwargs):
    course_obj=services.get_course_detail(course_id=course_id)
    if course_obj is None:
        raise Http404
    lessson_query_set=course_obj.lesson_set.all()

    return JsonResponse({"data":course_obj.id,"lesson_ids":[x.path for x in lessson_query_set]})
    return render(request,"courses/detail.html",{})

def lesson_detail_view(request,course_id=None,lesson_id=None,*args, **kwargs):
    print(lesson_id,course_id)
    lesson_obj=services.get_lessson_detail(course_id=course_id,lesson_id=lesson_id)
    if lesson_obj is None:
        raise Http404
    
    return JsonResponse({"data":lesson_obj.id})
    return render(request,"courses/lesson.html",{})

