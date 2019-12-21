from django.shortcuts import render
from django.http import HttpResponse
from .models import MyVideo


def hello(request):
	response = {}
	response['all_video'] = MyVideo.objects.all()
	return render(request, "index.html", response)
# Create your views here.
