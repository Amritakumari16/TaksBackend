# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# import Http Response from django
from django.http import HttpResponse
# get datetime
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
# create a function
from models import Employee
import json
class Authencate_User(APIView):
    def get(self, request):
        user_name = request.GET.get("username")
        password = request.GET.get("password")

        user_obj = authenticate(username=user_name, password=password)
        if user_obj:
            result = {"status": False, "message": "Invalid user"}
        else:
            result = {"status": False, "message": "Invalid user"}
        return Response(result)

class Employee_Data(APIView):
    def post(self, request):
        emp_file = request.FILES['data']
        emp_data = json.loads(emp_file)
        for each_emp in emp_data:
            emp_obj = Employee(first_name=each_emp.get("first_name"), last_name=each_emp.get("last_name"),
                               job_title=each_emp.get("job_title"), designation=each_emp.get("designation"))
            emp_obj.save()
        return Response("Employee Data Inserted Successfully")

    def get(self, request):

        all_employess = list(Employee.objects.all().values())
        return Response(all_employess)



