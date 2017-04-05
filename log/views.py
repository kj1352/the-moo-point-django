#!python
#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from log.models import Post
from django.http import HttpResponseRedirect
from django.utils import timezone

# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
	return render(request,"home.html")

def post(request):

    if request.POST:
        name = request.POST["name"]
        usn = request.POST["usn"]
        topic = request.POST["topic"]
        title = request.POST["title"]
        text = request.POST["text"]
        new_post = Post(name = name, usn = usn, topic = topic, title = title, text = text)
        new_post.save()
        return HttpResponseRedirect("/")
    return render(request,"home.html")

def see(request):
    posts = Post.objects.all()
    return render(request, 'list.html', {'posts': posts})