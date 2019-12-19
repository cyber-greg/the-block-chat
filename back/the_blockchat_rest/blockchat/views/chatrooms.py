from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from ..models import Chatroom
from django.core import serializers


@csrf_exempt  # ! FOR TEST PURPOSE ONLY - REMOVE IN PROD
def chatrooms(request):

    if request.method == 'GET':
       chatroomID = request.GET.get('id', None)
       userID = request.GET.get('user', None)

       print("GET CHATROOM FROM ID >>> {}".format(chatroomID))

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

    if chatroomID:
        response = Chatroom.objects.filter(id=chatroomID)
    elif userID:
        response = Chatroom.objects.filter(chatroom__id__contains=channelID)
    else:
        response = Chatroom.objects.all()

    data = serializers.serialize('json', response)
    return HttpResponse(data, content_type="application/json")
