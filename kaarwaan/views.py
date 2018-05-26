from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.decorators.cache import never_cache

from .models import School, Student, Mark

# Create your views here.
@never_cache
def data(request):
    school_list = School.objects.all()
    return render(request, 'kaarwaan/data.html', {'school_list': school_list, 'error_message': request.session.pop('error_message', None)})

@never_cache
def school_detail(request):
    if request.POST['school']:
        school = get_object_or_404(School, pk=request.POST['school'])
        request.session['school_id'] = school.id
    elif request.session.get('school_id'):
        school = get_object_or_404(School, pk=request.session.pop('school_id'))
    return render(request, 'kaarwaan/students.html', {'school': school, 'student_list': school.student_set.all(), 'error_message': None})

@never_cache
def result(request):
    if request.POST['student']:
        student = get_object_or_404(Student, pk=request.POST['student'])
        school = student.school
    return render(request, 'kaarwaan/result.html', {'marks_list': student.mark_set.all(), 'student': student, 'school': school})
