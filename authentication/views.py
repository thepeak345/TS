from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import logout, authenticate, login
from .forms import SignUpForm, LoginForm, OtpForm, PasswordResetForm
from .utils import generate_otp
from django.views import generic

User = get_user_model()


def signup(request):
    form = SignUpForm(request.POST or None)
    error = ''
    if request.method == 'POST':

        print(form.as_p())

        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(
                email=cd['email'],
                firstname=cd['firstname'],
                lastname=cd['lastname'],
                password=cd['password']
            )
            otp = generate_otp(5)
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
            return redirect('layout')
    return render(request, template_name='authentication/otp.html', context={
        'form': form,
    })


def login_view(request):
    form = LoginForm(request.POST or None)
    error = ''
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None and user.is_active:
                login(request, user)
                return redirect('layout')
    return render(request, 'authentication/login.html', context={
        'form': form,
        'error': error
    })


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')


class PasswordResetDoneView(generic.TemplateView):
    template_name = 'authentication/password_reset_done.html'
    title = "Password reset sent"


class PasswordResetView(generic.FormView):
    model = User
    template_name = 'authentication/password_reset.html'
    form_class = PasswordResetForm
