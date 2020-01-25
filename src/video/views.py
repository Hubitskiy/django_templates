from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MyVideo, Comment
import logging
from rest_framework.decorators import api_view
from django.core.cache import cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from video.forms import CommentForm, VideoForm, NeEbstisVideo


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
	response['form_video_creater'] = VideoForm()
	response['NeEbstisVideo'] = NeEbstisVideo()
	return render(request, "all_video.html", response)


def show_one(request, slug):
	response = {}
	logging.warning(slug)
	one_video = MyVideo.objects.get(slug=slug)
	response['all_video'] = [one_video.to_json()]
	return render(request, "all_video.html", response)


def add_comment(request, slug):
	text = request.POST['text']
	video = MyVideo.objects.get(slug=slug)
	comment = Comment.objects.create(
		text=text,
		video=video,
		user=request.user)
	return redirect('hello_url')

# def form_comment(request, slug):
# 	form = CommentForm(request.POST)
# 	if  form.is_valid():
# 		text = form.cleaned_data['text']
# 		vidosik = MyVideo.objects.get(slug=slug)
# 		user = request.user
# 		Comment.objects.create(
# 			text=text,
# 			video=vidosik,
# 			user=user)
# 	return redirect('hello_url')

def form_comment(request, slug):
	form = CommentForm(request.POST)
	video_id = MyVideo.objects.get(slug=slug).id
	if form.save(user_id=request.user.id, video_id=video_id):
		return redirect('hello_url')
	return HttpResponse('Error')
# Create your views here.


def form_video_creater(request,):
	video_form = VideoForm(request.POST)
	if video_form.save():
		return redirect('hello_url')
	return HttpResponse('Error')
