from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='')
    password = forms.CharField(label='', widget=forms.PasswordInput())


class RegisterForm(forms.Form):

    username = forms.CharField(max_length=50, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Kullanıcı Adı'}))
    password = forms.CharField(
        max_length=20, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Şifre'}))
    confirm = forms.CharField(
        max_length=20, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Şifre Tekrarı'}))

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor.")

        values = {
            "username": username,
            "password": password,
            "confirm": confirm,
        }

        return values
