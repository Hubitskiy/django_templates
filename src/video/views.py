from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MyVideo, Comment
import logging
from rest_framework.decorators import api_view
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from video.forms import CommentForm


def hello1(request):
	response = {}
	all_video = MyVideo.objects.all()
	response['all_video'] = [video.to_json() for video in all_video]
	return render(request, "all_video.html", response)


@api_view(['GET'])
def hello(request):
	response = {}
	#if "all_video" in cache:
	#	response['all_video'] = cache.get('all_video')
	#else:
	all_video = MyVideo.objects.all()
	all_video = [video.to_json() for video in all_video]
	#cache.set('all_video', all_video, timeout=DEFAULT_TIMEOUT)
	response['all_video'] = all_video
	response['form'] = CommentForm()
	response['flag'] = False
	return render(request, "all_video.html", response)


def show_one(request, slug):
	response = {}
	logging.warning(slug)
	one_video = MyVideo.objects.get(slug=slug)
	response['all_video'] = [one_video.to_json()]
	return render(request, "all_video.html", response)


def add_comment(request, slug):
	text = request.GET['text']
	video = MyVideo.objects.get(slug=slug)
	comment = Comment.objects.create(
		text=text,
		video=video,
		user=request.user)
	return redirect('hello_url')
# Create your views here.
