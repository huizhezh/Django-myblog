from django.shortcuts import render, get_object_or_404
from django.template import loader, Context
from django.http import HttpResponse
from blog.models import BlogPost


def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
    c = ({})
    # c = ({Context({'posts': posts})})
    # return HttpResponse(t.render(c))
    return render(request, "archive.html", {'posts': posts})


def post_pk(request, pk='1'):
    print(pk)
    posts = get_object_or_404(BlogPost, id=pk)
    print(posts.title)
    # t = loader.get_template('archive.html')
    # c = ({Context({'posts': post})})
    # return HttpResponse(t.render(c))
    return render(request, "archive_id.html", {'posts': posts})
    # return render(request, "archive.html", {'posts': posts})
