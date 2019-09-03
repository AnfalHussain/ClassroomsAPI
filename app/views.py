from django.shortcuts import render

# Create your views here.
from rest_framework.generics import (ListAPIView, RetrieveAPIView, 
    RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView)

from classes.models import Classroom

from .serializers import (ClassroomListSerializer,
ClassroomDetailSerializer)


class ClassroomListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomListSerializer



class ClassroomDetails(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


class UpdateClassroom(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


class CancelClassroom(DestroyAPIView):
    queryset = Classroom.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


class CreateClassroom(CreateAPIView):
    serializer_class = ClassroomDetailSerializer

    def perform_create(self, serializer):
    	serializer.save(teacher=self.request.user )



