from django import forms
from libapp.models import Suggestion, Libuser

TYPE_CHOICES = (
    (1, 'Book'),
    (2, 'DVD'),
    (3, 'Other'),
)

class SuggestionForm(forms.ModelForm):
   class Meta:
        model = Suggestion
        exclude = ['num_interested']
        labels = {'cost':'Estimated Cost in Dollars'}

        title = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'max_length': 100}))
        pubyr = forms.IntegerField(widget=forms.NumberInput())
        type = forms.RadioSelect()
        cost = forms.IntegerField(widget=forms.NumberInput())
        comments = forms.CharField(widget=forms.Textarea())

class SearchlibForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter Title"}),label='',required=False)
    author = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Enter Author/Maker"}), label='',required=False)

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'required': True, 'class': 'validate', 'placeholder': 'Username'}), label="")
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'required': True, 'class': 'validate input-field', 'placeholder': 'Password'}),
        label="")
#
# class Register(forms.ModelForm):
#     class Meta:
#         model = Libuser
#         fields = ['username', 'password', 'password1', 'first_name', 'last_name', 'email', 'address', 'city', 'province',
#                   ]
#
#
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'validate'}), label="Password")
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'validate'}), label="Confirm Password")

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Libuser
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        exclude = ['address', 'city', 'province']
    username = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'max_length': 200}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'required': True, 'max_length': 200}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'max_length': 200}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'max_length': 200}))
    email = forms.CharField(widget=forms.TextInput(attrs={'required': True, 'max_length': 200}))
