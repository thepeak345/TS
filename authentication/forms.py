from django import forms


class SignUpForm(forms.Form):
    email = forms.EmailField()
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.name


class LoginForm(forms.Form):
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class OtpForm(forms.Form):
    otp = forms.IntegerField()
