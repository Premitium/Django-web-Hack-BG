from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    return render(request, 'onmarket/index.html', locals())

#
# def index(request):
#     if not request.session.get('counter'):
#         request.session['counter'] = 0
#
#     request.session['counter'] += 1
#
#     posts = BlogPost.objects.all()
#     tags = Tag.objects.all()
#
#     return render(request, 'blog/index.html', locals())
