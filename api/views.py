#from django.shortcuts import render
from .serializer import StudentSerializer
from .models import StudentModel
#from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.

# generic view classes
# CRUD operation at seperate page or at seperate urls






# start of combination apiviews
#  combination of APIViews like listCreateAPIViews



class Studentapi_List_Create(ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer


class Studentapi_Read_Update_Delete(RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer            

# end of combination of APIViews    
