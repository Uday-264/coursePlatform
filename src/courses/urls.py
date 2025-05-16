from django.urls import path,include
from django.conf import settings
# from django.conf.urls.static import static

from . import views 
urlpatterns = [
    path('',views.course_list_view),
    path('<slug:course_id>/',views.course_detail_view),
    path('<slug:course_id>/lessons/<slug:lesson_id>/',views.lesson_detail_view),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)