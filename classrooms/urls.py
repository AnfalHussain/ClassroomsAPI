
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from classes import views
from app.views import ( ClassroomListView, ClassroomDetails, 
    UpdateClassroom, CancelClassroom, CreateClassroom) 

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),
    


    path('classroomsAPI/', ClassroomListView.as_view(), name="Classroom-list"), 
    path('classroomsAPI/<int:classroom_id>/', ClassroomDetails.as_view(), name="Classroom-details"),
    path('classroomsAPI/<int:classroom_id>/update/', UpdateClassroom.as_view(), name="Classroom-booking"),
    path('classroomsAPI/<int:classroom_id>/cancel/', CancelClassroom.as_view(), name="cancel-class"),
    path('classroomsAPI/create/', CreateClassroom.as_view(), name="create-class"),
    
    path('api/token/', TokenObtainPairView.as_view(), name='login'),

]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
