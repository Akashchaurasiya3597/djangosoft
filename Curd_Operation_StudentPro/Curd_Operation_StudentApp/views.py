from django.shortcuts import render,redirect
from .models import Studentdatabase


def Homepage_view(request):
    student = Studentdatabase.objects.all()
    context = {'student': student}
    return render(request, 'Homepage.html', context)


def Student_create_view(request):
    context = {}
    return render(request,'student_create.html',context)


def Insert_data(request):

    Roll_number = request.POST.get('Roll_number')
    First_name = request.POST.get('First_name')
    Last_name = request.POST.get('Last_name')
    Email = request.POST.get('Email')
    School_name = request.POST.get('School_name')
    Class_name = request.POST.get('Class_name')
    Section_name = request.POST.get('Section_name')
    Telugu_marks = request.POST.get('Telugu_marks')
    Hindi_marks = request.POST.get('Hindi_marks')
    English_marks = request.POST.get('English_marks')
    Maths_marks = request.POST.get('Maths_marks')
    Science_marks = request.POST.get('Science_marks')
    Social_marks = request.POST.get('Social_marks')

    data = Studentdatabase(
        Roll_number=Roll_number,
        First_name=First_name,
        Last_name=Last_name,
        Email=Email,
        School_name=School_name,
        Class_name=Class_name,
        Section_name=Section_name,
        Telugu_marks=Telugu_marks,
        Hindi_marks=Hindi_marks,
        English_marks=English_marks,
        Maths_marks=Maths_marks,
        Science_marks=Science_marks,
        Social_marks=Social_marks
    )
    data.save()
    return redirect('/')


def update_view(request,pk):
    student = Studentdatabase.objects.get(id=pk)
    context = {'student':student}
    return render(request, 'student_update.html',context)


def replace_view(request,pk):
    student = Studentdatabase.objects.get(id=pk)
    student.Roll_number = request.POST.get('Roll_number')
    student.First_name = request.POST.get('First_name')
    student.Last_name = request.POST.get('Last_name')
    student.Email = request.POST.get('Email')
    student.School_name = request.POST.get('School_name')
    student.Class_name = request.POST.get('Class_name')
    student.Section_name = request.POST.get('Section_name')
    student.Telugu_marks = request.POST.get('Telugu_marks')
    student.Hindi_marks = request.POST.get('Hindi_marks')
    student.English_marks = request.POST.get('English_marks')
    student.Maths_marks = request.POST.get('Maths_marks')
    student.Science_marks = request.POST.get('Science_marks')
    student.Social_marks = request.POST.get('Social_marks')
    student.save()
    return redirect('/')


def delete_view(request,pk):
    student = Studentdatabase.objects.get(id=pk)
    student.delete()
    return redirect('/')