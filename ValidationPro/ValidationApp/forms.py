from django import forms
from .models import RegistrationModel

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationModel
        fields = '__all__'


    def clean_username(self):
        super(RegistrationForm, self).clean()
        username = self.cleaned_data.get('username')

        user = RegistrationModel.objects.filter(username=username)


        if user.exists():
            raise forms.ValidationError('user name is taken Allready')
        elif len(str(username)) <= 5 or len(str(username)) >= 15:
            raise forms.ValidationError('user name must have more then 5 character less then 15')



        return self.cleaned_data

