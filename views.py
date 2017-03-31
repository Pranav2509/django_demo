from django.http import HttpResponse
import json
from models import *

def get_student_data(request):
    students = student_data.objects.all()

    response_data = {}
    student_details = []

    for student in students:
        single_student_json = {}
        single_student_json['roll_no'] = student.roll_no
        single_student_json['stud_name'] = student.stud_name
        single_student_json['stud_sub1'] = student.stud_sub1
        single_student_json['stud_sub2'] = student.stud_sub2
        single_student_json['stud_sub3'] = student.stud_sub3
        single_student_json['stud_sub4'] = student.stud_sub4
        single_student_json['stud_sub5'] = student.stud_sub5
        single_student_json['stud_avg'] = student.stud_avg

        student_details.append(single_student_json)

    response_data['student_details']= student_details
    response_data['response_status'] = 2
    response_data['error_status'] = 0
    response_data['response_msg'] = 'student data is fetched'

    return HttpResponse(json.dumps(response_data), content_type="application/json")
