from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    context = {
        'Judul': 'blog1',
        'h1': 'Rifqi Fathurrohman',
        'menu': [['blog/', 'Home'], ['blog/recent'], ['/post', 'Post']]
    }
    return render(request, 'blog/index.html', context)


def recent(request):
    # context = {
    #    'Judul': 'Identitas Diri',
    #    'h1': 'Rifqi Fathurrohman',
    #    'h2': '16 Maret 2001',
    #    'h3': 'Dki Jakarta, Jakarta timur'
    # }
    # return render(request, 'blog/index.html', context)

    return HttpResponse("RECENT BLOG")
