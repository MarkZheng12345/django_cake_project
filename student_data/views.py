from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Course, Student
# Create your views here.

def student_all(request):
    students = Student.objects.all().values('sid')

    students = Student.objects.filter(sid='S002', course_id='C001').values()
    students = Student.objects.filter(Q(sid='S002') | Q(course_id='C001')).values()
    students = Student.objects.filter(Q(name='John') | Q(name='Mark')).values()
    # select * from Student where name like 'J%'
    students = Student.objects.filter(Q(name__startswith='J') | Q(course_id='C001')).values()
    students = Student.objects.select_related('course').get(course_name='java').values()
    #students = students.course.course_name

    context = {'students': students}
    return render(request, 'experience.html', context=context)


def student_info(request):
    course1 = Course(course_id='C001', course_name='python', duration='30')
    course1.save()

    course_instance = Course.objects.get(course_id='C001')
    student1 = Student(sid='S001', name='Mark', course=course_instance)
    student1.save()

    fetch1 = Student.objects.get(name='John')
    fetch_name = fetch1.course.course_name
    print("....................course for user is ", fetch_name)

    #Course.objects.filter(course_id='C002').delete()
    messages = ['Course and student are added']

    return render(request, 'experience.html', {'messages': messages})
    #return redirect('/')
