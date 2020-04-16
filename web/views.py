from datetime import datetime

from django.conf import settings
from django.forms import model_to_dict
from django.shortcuts import render, redirect

from web.models import Publication


def index(request):
    return render(request, 'index.html')


def contacts(request):
    return render(request, 'contacts.html')


def publication(request, number):
    pubs = Publication.objects.filter(id=number)
    if len(pubs) == 0:
        return redirect('/')
    else:
        pub = model_to_dict(pubs[0])
        return render(request, 'publication.html', pub)


def publications(request):
    return render(request, 'publications.html', {
        'publications': Publication.objects.all()
    })


def publish(request):
    if request.method == 'GET':
        return render(request, 'publish.html')
    else:
        secret = request.POST['secret']
        name = request.POST['name']
        text = request.POST['text']
        if secret != settings.SECRET_KEY:
            return render(request, 'publish.html', {
                'error': "incorrect secret key"
            })
        if len(name) == 0:
            return render(request, 'publish.html', {
                'error': "empty name"
            })
        if len(text) == 0:
            return render(request, 'publish.html', {
                'error': "empty text publication"
            })

        Publication(name=name, date=datetime.now(), text=text.replace('\n', '<br>')).save()
        return redirect('/publications')