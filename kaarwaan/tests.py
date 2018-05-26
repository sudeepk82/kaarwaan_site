from django.test import TestCase
from django.urls import reverse

from .models import School, Student
# Create your tests here.

def create_school(school_name,):
    return School.objects.create(school_name=school_name)

def create_student(school_name, student_name, dob):
    school = School.objects.filter(school_name=school_name) 
    return Student.objects.create(school=school, student_name=student_name, student_dob=dob)

class SchooldataTests(TestCase):
    def test_no_schools(self):
        response = self.client.get(reverse('kaarwaan:data'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No schools available.")
        self.assertQuerysetEqual(response.context['school_list'], [])
    
    def test_schools(self):
        create_school(school_name="school1",)
        response = self.client.get(reverse('kaarwaan:data'))
        self.assertQuerysetEqual(
            response.context['school_list'],
            ['<School: school1>']
        )

#class studentsTests(TestCase):
#    def test_school_with_no_students(self):
#        create_school(school_name="school2")

#        response = self.client.get(reverse('kaarwaan:data'))
#        self.assertQuerysetEqual(
#            response.context['school_list'],
#            ['<School: school2>']
#        )
#        school = response.context['school_list']
#        response = self.client.post(reverse('kaarwaan:students'),  data={'school':school[0].id,})
#        self.assertEqual(response.status_code, 200)
#        self.assertContains(response, "No students available.")
#        self.assertListEqual(response.student_list, [])

#    def test_school_with_students():

#class MarksresultTests(TestCase):
#    def test_student_with_no_marks(self):
#
#    def test_student_with_marks(self):

