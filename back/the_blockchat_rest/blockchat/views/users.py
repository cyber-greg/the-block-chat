from django.core import serializers
from ..models import Message
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
User = get_user_model()


@csrf_exempt  # ! FOR TEST PURPOSE ONLY - REMOVE IN PROD
def users(request):

    if request.method == 'GET':
        userID = request.GET.get('id', None)
    #    channelID = channel
        print("GET USER FROM ID >>> {}".format(userID))

    elif request.method == 'POST':
        pass
        # data = json.loads(request.body)
        # print("CONTENT >>> {}".format(data['content']))
        # channelID = data['channel']
        # new_message = Message(
        #     content=data['content'],
        #     date=data['date'],
        #     author=data['author'],
        #     channel=data['channel'] # ! get channel from channelID
        # )
        # new_message.save()

    if userID:
        response = User.objects.filter(id=userID)
    else:
        response = User.objects.all()

    parsed_response = []

    for user in response:
        parsed_response.append({
            "id": str(user.pk),
            "pseudo": user.full_name,
            "email": user.email

        })

    return JsonResponse(parsed_response, safe=False, json_dumps_params={'ensure_ascii': False})
