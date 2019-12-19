from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment, MyVideo


def hello(request):
	return render(request, "index.html")
# Create your views here.
