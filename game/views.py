from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import BoxForm, CodeboxForm
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
                return redirect('layout')
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
    form = CodeboxForm(request.POST or None)
    title = request.session.get('title')
    box = Box.objects.get(title=title)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            if cd['start_date'] == box.start_date:
                box.is_active = True
                box.save()
                del request.session['title']
            return redirect('home')
    return render(request, template_name='game/codebox.html', context={
        'form': form,
    })
