from django.core import serializers
from ..models import Message
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
User = get_user_model()


@csrf_exempt  # ! FOR TEST PURPOSE ONLY - REMOVE IN PROD
def login(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        print("CONTENT >>> {} / {}".format(data['email'], data['password']))
        user_email = data['email']

        user = User.objects.get(email=user_email)
        print(user)
        print(user.password)
        password_match = check_password(data['password'], user.password)
        print(password_match)
        if password_match:
            return HttpResponse("{}".format(user.id))


    return HttpResponseForbidden()


