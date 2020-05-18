from django.shortcuts import render,HttpResponse
from django.http.response import HttpResponse
from .models import RegistrationModel
from .forms import RegistrationForm

# Create your views here.
def Register_view(request):
    if request.method == 'POST':
        Rform = RegistrationForm(request.POST)
        if Rform.is_valid():
            Rform = Rform.save(commit=False)
            Rform.save()
            Rform = RegistrationForm()
            context = {'Rform': Rform}
            return render(request, 'Registeration.html', context)
        else:

            context = {'Rform': Rform}
            return render(request, 'Registeration.html', context)
    else:
        Rform = RegistrationForm()
        context = {'Rform':Rform}
        return render(request,'Registeration.html',context)
