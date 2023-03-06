from django.shortcuts import render
from django.urls import reverse

from .forms import BoxForm
from .models import Box
from authentication.utils import generate_otp
from game.models import Box

from django.contrib.auth.decorators import login_required


@login_required
def create_box(request):
    try:
        box = Box.objects.get(member=request.user)
        message = 'Вы уже являетесь игроком игры {}'.format(box.title)
        form = None
    except Box.DoesNotExist:
        message = None
        form = BoxForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                cd = form.cleaned_data
                box = Box.objects.create(
                    size=cd['size'],
                    member=request.user,
                    is_owner=True
                )
                if cd['is_closed']:
                    otp = generate_otp(10)
                    box.code = otp
                    print(otp)
                    box.save()

    context = {
        'form': form,
        'message': message
    }
    return render(request, 'check.html', context)


def box_title(request):
    return render(request, 'game/game_title.html', context={
        'title': 'title'
    })


def box_confirm(request):

