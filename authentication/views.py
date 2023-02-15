from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import logout, authenticate, login
from .forms import SignUpForm, LoginForm, OtpForm
from .utils import generate_otp

User = get_user_model()


def signup(request):
    form = SignUpForm(request.POST or None)
    error = ''
    if request.method == 'POST':

        print(form.as_p())

        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                firstname=cd['firstname'],
                lastname=cd['lastname'],
                email=cd['email'],
                password=cd['password']
            )
            otp = generate_otp()
            user.otp = otp
            print(otp)
            user.save()
            request.session['email'] = user.email

            return redirect('otp')

    return render(request, template_name='authentication/signup.html', context={
        'form': form,
        'title': 'Signup',
        'error': error
    })


def user_confirm(request):
    form = OtpForm(request.POST or None)
    email = request.session.get('email')
    user = User.objects.get(email=email)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            if cd['otp'] == user.otp:
                user.is_active = True
                user.save()
                del request.session['email']
            return redirect()
    return render(request, template_name='authentication/otp.html', context={
        'form': form,
    })


def login_view(request):
    form = LoginForm(request.POST or None)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(firstname=cd['firstname'], lastname=cd['lastname'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('success')
    return render(request, 'authentication/login.html', context={
        'form': form,
        'error': error
    })


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')
