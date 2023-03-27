from django.shortcuts import render


def index(request):
    return render(request, 'layout.html', context={
        'title': 'Home'
    })
