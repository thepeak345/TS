from django.shortcuts import render
from django.urls import reverse

from .forms import BoxForm
from .models import Box


def create_box(request):
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
                # Пусть будет редирект,
                # где нужно будет генерировать кодовое слово
                pass

    context = {
        'form': form,
    }
    return render(request, 'check.html', context)
