from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

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
                box = Box.objects.create(size=cd['size'])
                if cd['is_closed']:
                    otp = generate_otp(10)
                    box.code = otp
                    print(otp)
                    box.save()
                request.user.box_owner = True
                request.user.save()
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


@login_required
def box_confirm(request):
    form = CodeboxForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            code = cd['codebox']
            try:
                box = Box.objects.get(code=code)
                request.user.box = box
                request.user.save()
                box.count += 1
                box.save()
                return redirect('layout')
            except Box.DoesNotExist:
                form = CodeboxForm()
                messages.error(request, message='Такой игры не существует')
    context = {
        'form': form,
    }
    return render(request, template_name='game/codebox.html', context=context)
