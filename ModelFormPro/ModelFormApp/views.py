from django.shortcuts import render
from .models import Customer_model
from .forms import Customer_Form
from django.http.response import HttpResponse


# Create your views here.
def home_view(request):
    if request.method == 'POST':
        aform = Customer_Form(request.POST, request.FILES)
        if aform.is_valid():
            Customer_name = aform.cleaned_data.get('Customer_name')
            Sales = aform.cleaned_data.get('Sales')
            Mobile_number = aform.cleaned_data.get('Mobile_number')
            Email = aform.cleaned_data.get('Email')
            Location = aform.cleaned_data.get('Location')
            picture = aform.cleaned_data.get('picture')
            data = Customer_model(
                Customer_name=Customer_name,
                Sales=Sales,
                Mobile_number=Mobile_number,
                Email=Email,
                Location=Location,
                picture=picture
            )
            data.save()
            aform = Customer_Form()
            context = {'aform': aform}
            return render(request, 'customer_page.html', context)
        else:
            return HttpResponse('invalid Data')
    else:
        aform = Customer_Form()
        context = {'aform': aform}
        return render(request, 'customer_page.html', context)
