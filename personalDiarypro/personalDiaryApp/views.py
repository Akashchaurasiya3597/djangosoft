from django.shortcuts import render,redirect
from .models import Dairy_model
from .forms import Diary_form
from django.http.response import HttpResponse




def home_view(request):
    context ={}
    return render(request,'Home_page.html',context)

def Dairy_view(request):
    show = Dairy_model.objects.all()
    context={'show':show}
    return render(request, 'Dairy_page.html', context)


def insert_view(request):
    if request.method == 'POST':
        insert = Diary_form(request.POST, request.FILES)
        if insert.is_valid():
            Title = insert.cleaned_data.get('Title')
            Description = insert.cleaned_data.get('Description')
            UploadSelfie = insert.cleaned_data.get('UploadSelfie')
            UploadImage1 = insert.cleaned_data.get('UploadImage1')
            UploadImage2 = insert.cleaned_data.get('UploadImage2')
            UploadImage3 = insert.cleaned_data.get('UploadImage3')
            data = Dairy_model(
               Title=Title,
               Description=Description,
               UploadSelfie=UploadSelfie,
               UploadImage1=UploadImage1,
               UploadImage2=UploadImage2,
               UploadImage3=UploadImage3,
            )
            data.save()
            insert = Diary_form()
            context = {'insert': insert}
            return render(request, 'Createpage.html', context)
    else:
        insert = Diary_form()
        context = {'insert':insert}
        return render(request,'Createpage.html',context)




def Update_view(request, pk):
    diary = Dairy_model.objects.get(id=pk)
    uform=Diary_form(instance=diary)
    if request.method == 'POST':
        uform=Diary_form(request.POST, request.FILES, instance=diary)
        if uform.is_valid():
            #edit = update.save(commit=False)
            uform.save()
            return redirect('/')
    context ={'uform':uform}
    return render(request, 'Upadte_page.html', context)


def delete_view(request,pk):
    dform = Dairy_model.objects.get(id=pk)
    dform.delete()
    context = {'dform':dform}
    return redirect('/')
