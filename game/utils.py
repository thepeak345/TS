import random
from game.models import Pair
from django.contrib.auth import get_user_model

User = get_user_model()
def box_pair(box):
    qs = list(User.objects.filter(box=box).values_list('id', flat=True))
    random.shuffle(qs)
    pairs = list(zip(qs[1::2], qs[::2]))
    for pair in pairs:
        player1, player2 = pair
        Pair.objects.create(box=box, player1=player1, player2=player2)

