from .models import Course,Lesson,publicStatus

def get_public_courses():
    return Course.objects.filter(status=publicStatus.PUBLISHED)

def get_course_detail(course_id=None):
    if course_id is None:
        return None
    obj=None
    try:
        obj=Course.objects.get(status=publicStatus.PUBLISHED,public_id=course_id)
    except:
        pass
    return obj

def get_lessson_detail(course_id=None,lesson_id=None):
    if lesson_id is None or course_id is None:
        return None
    obj=None
    try:
        obj=Lesson.objects.get(
            course__public_id=course_id,
            course__status=publicStatus.PUBLISHED,
            status=publicStatus.PUBLISHED,
            public_id=lesson_id
        )
    except Exception as e:
        print("lesson detail",e)
        
    return obj