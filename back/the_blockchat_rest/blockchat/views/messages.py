from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from ..models import Message
from django.core import serializers


@csrf_exempt  # ! FOR TEST PURPOSE ONLY - REMOVE IN PROD
def messages(request):

    if request.method == 'GET':
        channelID = request.GET.get('channel', None)
    #    channelID = channel
        print("GET MESSAGES FROM CHANNEL >>> {}".format(channelID))

    elif request.method == 'POST':
        data = json.loads(request.body)
        print("CONTENT >>> {}".format(data['content']))
        channelID = data['channel']
        new_message = Message(
            content=data['content'],
            date=data['date'],
            author=data['author'],
            channel=data['channel']  # ! get channel from channelID
        )
        new_message.save()

    response = []
    if channelID:
        response = Message.objects.filter(channel__id__contains=channelID)

    data = serializers.serialize('json', response)
    return HttpResponse(data, content_type="application/json")
