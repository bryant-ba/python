from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogPost
from django.template import loader,Context

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))