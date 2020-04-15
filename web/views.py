from datetime import datetime

from django.conf import settings
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def contacts(request):
    return render(request, 'contacts.html')


publications_data = [
    {
        'id': 0,
        'name': "My first publication",
        'date': datetime.now(),
        'text': '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Purus ut faucibus pulvinar elementum integer enim neque volutpat ac. Posuere ac ut consequat semper viverra nam libero. Habitasse platea dictumst quisque sagittis purus sit. A erat nam at lectus urna. Quis blandit turpis cursus in hac. Varius duis at consectetur lorem donec. Est velit egestas dui id ornare arcu. Urna nunc id cursus metus aliquam eleifend mi in nulla. Lectus nulla at volutpat diam ut.
                   <br><br>Mauris sit amet massa vitae. Vitae ultricies leo integer malesuada nunc vel risus commodo. Accumsan sit amet nulla facilisi morbi tempus. A erat nam at lectus urna duis. Nibh tellus molestie nunc non. Sed odio morbi quis commodo odio aenean sed adipiscing diam. Lectus urna duis convallis convallis. Penatibus et magnis dis parturient montes nascetur ridiculus mus mauris. Amet nisl suscipit adipiscing bibendum. Facilisis volutpat est velit egestas. Enim ut tellus elementum sagittis vitae. Quis risus sed vulputate odio ut. Senectus et netus et malesuada fames ac turpis egestas maecenas. Pulvinar neque laoreet suspendisse interdum consectetur libero id faucibus. Non enim praesent elementum facilisis leo vel. Massa id neque aliquam vestibulum morbi.'''
    },
    {
        'id': 1,
        'name': "My second publication",
        'date': datetime.now(),
        'text': '''Section 1.10.32 of "de Finibus Bonorum et Malorum", written by Cicero in 45 BC
                   <br><br>"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"'''
    },
    {
        'id': 2,
        'name': "My third publication",
        'date': datetime.now(),
        'text': '''Section 1.10.32 of "de Finibus Bonorum et Malorum", written by Cicero in 45 BC
                   <br><br>"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"'''
    }
]


def publication(request, number):
    if number < len(publications_data):
        return render(request, 'publication.html', publications_data[number])
    else:
        return redirect('/')


def publications(request):
    return render(request, 'publications.html', {
        'publications': publications_data
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

        publications_data.append({
            'id': len(publications_data),
            'name': name,
            'date': datetime.now(),
            'text': text.replace('\n', '<br>')
        })
        return redirect('/publications')