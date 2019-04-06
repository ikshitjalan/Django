from django import forms
from django.core import validators
from first_app.models import User

def  check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name should start with letter "z"')


class FormName(forms.Form):
    name = forms.CharField(validators = [check_for_z])
    email = forms.EmailField()
    email_verif = forms.EmailField(label = "Verify your email!")
    text = forms.CharField(widget = forms.Textarea)
    bot_catcher = forms.CharField(required = False,widget= forms.HiddenInput,
                                        validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['email_verif']

        if email != vmail:
            raise forms.ValidationError("Emails Donot Match!")

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
