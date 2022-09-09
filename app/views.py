from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
# Create your views here.



from . serializer import *
from . models import *


class Statedetails(ListCreateAPIView):
    queryset = ""
    serializer_class = stateSerializer



class citydetails(ListCreateAPIView):
    queryset = ""
    serializer_class = citySerializer


class towndetails(ListCreateAPIView):
    queryset = ""
    serializer_class = townSerializer

    