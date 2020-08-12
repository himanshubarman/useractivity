from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED
)
from django.http import HttpResponse
from .models import User, UserActivity
from datetime import timedelta,datetime
import os

# User Activity Api displaying the required JSON data
class UserView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):

        timestamp_format = "%b %d %Y %I:%M%p"
        users = User.objects.all()
        activity = UserActivity.objects.all()
        result = []
        for i in activity:
            user_exists = [e for e in result if e['id'] == i.user.id]
            if user_exists:
                periods = user_exists[0].get('activity_periods')
                start_time = self.change_time_format(i.start_time)
                end_time = self.change_time_format(i.end_time)
                periods.append({'start_time' : start_time, 'end_time' : end_time})
            else:
                temp = {}
                temp['real_name'] = i.user.real_name
                temp['id'] = i.user.id
                temp['tz'] = i.user.tz
                start_time = self.change_time_format(i.start_time)
                end_time = self.change_time_format(i.end_time)
                temp['activity_periods'] = [{'start_time' : start_time, 'end_time' : end_time}]
                result.append(temp)

        return Response(result, status=HTTP_200_OK)

    def change_time_format(self, data):
        _timestamp = datetime.strptime(data.strftime("%Y-%m-%dT%H:%M:%S%z"),"%Y-%m-%dT%H:%M:%S%z")
        timestamp = _timestamp.strftime("%b %d %Y %I:%M%p")
        return timestamp

# if value of check is 0 the command executed successfully
# after the generatedata --> (3) is the paramter the number of user to be created
def generatedata(request):

    check = os.system("python3 manage.py generatedata 3")
    
    user_data = User.objects.filter().values()
    return HttpResponse(user_data)