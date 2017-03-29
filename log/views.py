#!python
#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from log.models import ContactUs
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
# this login required decorator is to not allow to any
# view without authenticating
@login_required(login_url="login/")
def home(request):
	return render(request,"home.html")


def contactus(request):
    from django.core.mail import send_mail
    if request.POST:
        name = request.POST["name"]
        title = request.POST["title"]
        text = request.POST["text"]
        new_contact = ContactUs(name = name,title = title, text = text)
        new_contact.save()
        send_mail("Contact The Number", "Name:" + name + "," + "title:" + title + "," + "Text:" + text, "nikhilkj24@gmail.com", ["kj@webtrigon.com"])
        return HttpResponseRedirect("/")
    return render(request,"home.html")
