from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import BoxForm, CodeboxForm
from authentication.utils import generate_otp
from game.models import Box
from authentication.models import CustomUser

from django.contrib.auth.decorators import login_required


@login_required
def create_box(request):
    if request.user.box is not None:
        box = Box.objects.get(pk=request.user.box.pk)
        message = 'Вы уже являетесь игроком игры {}'.format(box.title)
        form = None
    else:
        message = None
        form = BoxForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                cd = form.cleaned_data
                box = Box.objects.create(
                    size=cd['size'],
                    title=cd['title']
                )
                if cd['is_closed']:
                    otp = generate_otp(10)
                    box.code = otp
                    print(otp)
                    box.is_closed = True
                    box.save()
                request.user.box_owner = True
                request.user.box = box
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
def box_confirm(request):   #Поиск закрытых игр
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
                return redirect('box_info', pk=box.pk)
            except Box.DoesNotExist:
                form = CodeboxForm()
                messages.error(request, message='Такой игры не существует')
    context = {
        'form': form,
    }
    return render(request, template_name='game/codebox.html', context=context)


def get_all_games(request):
    boxes = Box.objects.filter(is_closed=False, is_active=True)
    context = {
        'boxes': boxes
    }
    return render(request, template_name='game/open_boxes.html', context=context)


@login_required
def exit_box(request):
    if request.user.box:
        box = Box.objects.get(pk=request.user.box.pk)
        request.user.box = None
        box.count -= 1
        if request.user.box_owner:
            request.user.box_owner = False
        request.user.save()
        box.save()

    return redirect('layout')


@login_required
def enter_box(request, pk):
    if not request.user.box:
        box = Box.objects.get(pk=pk)
        request.user.box = box
        box.count += 1
        request.user.save()
        box.save()
        if box.count == box.size:
            box.is_active = False
            return redirect('start_game')
    return redirect('layout')


def box_info(request, pk):
    box = Box.objects.get(pk=pk)
    context = {
        'count': box.count,
        'title': box.title,
        'size': box.size,
        'pk': pk
    }
    return render(request, template_name='game/box_inf.html', context=context)

# def end(request):
#     boxes = CustomUser.objects.select_related('box').filter(box=request.user.box)

def preferences_box(request):
    preferences = CustomUser.preferences
    return render(request, 'game/start_game.html', context={
        'preferences': preferences,
    })