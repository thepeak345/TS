from django.shortcuts import render
from django.urls import reverse

from .forms import BoxForm
from .models import Box
from authentication.utils import generate_otp


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
                otp = generate_otp(10)
                box.code = otp
                box.save()

    context = {
        'form': form,
    }
    return render(request, 'check.html', context)
