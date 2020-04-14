from django.http import HttpResponse


def index(request):
    return HttpResponse('''Hello world!<br>
        <a href="./status">Status</a>''')


def status(request):
    return HttpResponse('''<H2>OK</H2><br>
        <a href="/">Return</a>''')
