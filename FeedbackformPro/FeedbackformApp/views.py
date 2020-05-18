from django.shortcuts import render
from .models import FeedbackDatabase
from .forms import FeedbackForm
from django.http.response import HttpResponse
import datetime

Data = datetime.datetime.now()
def feedback_view(request):
    if request.method == 'GET':
        fform = FeedbackForm()
        feedback = FeedbackDatabase.objects.all()
        return render(request, 'Feedback_Form.html',{'fform': fform , 'feedback':feedback})
    else:
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            First_name = request.POST.get('First_name')
            Last_name = request.POST.get('Last_name')
            Email = request.POST.get('Email')
            Mobile = request.POST.get('Mobile')
            ratting = request.POST.get('ratting')
            Feedback = request.POST.get('Feedback')
            data = FeedbackDatabase(
                First_name=First_name,
                Last_name=Last_name,
                Email=Email,
                Mobile=Mobile,
                ratting=ratting,
                Data=Data,
                Feedback=Feedback
            )
            data.save()
            fform = FeedbackForm()
            feedback=FeedbackDatabase.objects.all()
            return render(request, 'Feedback_Form.html', {'fform': fform , 'feedback':feedback})

        else:
            return HttpResponse('Invalid Data')