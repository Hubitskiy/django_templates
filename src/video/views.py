from django.shortcuts import render
from django.http import HttpResponse
from .models import MyVideo
import logging
from rest_framework.decorators import api_view
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT


def hello1(request):
	response = {}
	all_video = MyVideo.objects.all()
	response['all_video'] = [video.to_json() for video in all_video]
	return render(request, "index.html", response)


@api_view(['GET'])
def hello(request):
	response = {}
	if "all_video" in cache:
		response['all_video'] = cache.get('all_video')
	else:
		all_video = MyVideo.objects.all()
		all_video = [video.to_json() for video in all_video]
		cache.set('all_video', all_video, timeout=DEFAULT_TIMEOUT)
		response['all_video'] = all_video
	return render(request, "index.html", response)


def show_one(request, slug):
	response = {}
	logging.warning(slug)
	one_video = MyVideo.objects.get(slug=slug)
	response['all_video'] = [one_video.to_json()]
	return render(request, "index.html", response)
# Create your views here.
