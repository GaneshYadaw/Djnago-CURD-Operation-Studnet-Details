from django.http import HttpResponseRedirect
from django.shortcuts import render

from curd_app.models import Student
from.forms import StudentRegistration

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            register = Student(name=name, email=email, address=address)
            register.save()
            form = StudentRegistration()
    else:
        form = StudentRegistration()
    student = Student.objects.all()
    return render(request, 'curd/addshow.html', {'form':form, 'student':student})

def delete(request, id):
    if request.method == 'POST':
        S1 = Student.objects.get(pk=id)
        S1.delete()
        return HttpResponseRedirect('/')
    
def update(request, id):
    if request.method =='POST':
        S2 = Student.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=S2)
        if form.is_valid():
            form.save()
    else:
        S2 = Student.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=S2)     
    return render(request, 'curd/update_student.html', {'form':form})
    