from django.shortcuts import render,redirect,get_object_or_404
from .models import Student
from .form import StudentForm

# Create your views here.
def student_list(request):
    student = Student.objects.all()
    return render(request,'student_list.html',{'student':student})  

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request,'student_create.html',{'form':form})
    
def student_edit(request,pk):
    student = get_object_or_404(Student,pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request,'student_create.html',{'form':form})

def student_delete(request,pk):
    student = get_object_or_404(Student,pk=pk)
    student.delete()
    return redirect('student_list')

def student_detail(request,pk):
    student = get_object_or_404(Student,pk=pk)
    return render(request,"student_detail.html",{'student':student})