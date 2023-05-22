from django.shortcuts import render
from game.models import Pair
from django.contrib.auth.models import AnonymousUser

def index(request):
    context = {'title': 'Home'}
    if not isinstance(request.user, AnonymousUser):
        pair = Pair.objects.filter(player1=request.user).order_by('-pk')
        pair2 = Pair.objects.filter(player1=request.user).order_by('-pk')
        if pair.exists():
            context.update(dict(user_pair=pair[0].player2))
        elif pair2.exists():
            context.update(dict(user_pair=pair2[0].player1))
    return render(request, 'layout.html', context=context)
