from django.shortcuts import render

def index(request):
    return render(request, 'main/home.html', context={
        'title': 'Home'
    })

