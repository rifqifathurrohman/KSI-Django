from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponse
from .models import Post


def index(request):
    db = Post.objects.all()
    context = {
        'Judul': 'Blog Saya',
        'h1': 'About Me',
        'Nama': 'Rifqi Fathurrohman',
        'NPM': '1204076',
        'Asal': 'Jakarta timur, DKI Jakarta',
        'Email': 'rifqifathurrohman236@gmail.com',
        'HP': '085156581959',
        'Umur': '21',
        'Desc': 'Mahasiswa Vokasi ULBI',
        'title': 'Blog',
        'heading': 'Blog',
        'subheading': 'postingan',
        'post': db,
    }

    return render(request, 'about/index.html', context)


def recent(request):
    return HttpResponse("RECENT ABOUT")
    # context = {
    #    'Judul' : 'blog2',
    #    'h1' : 'Python'
    # }
    # return render(request, 'blog/index.html', context)
# Create your views here
