from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
User = get_user_model()

import json

from ..models import Message, Channel
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
        authorID = data['author']

        # get objects from ID
        query_author = User.objects.filter(pk=authorID)
        query_channel = Channel.objects.filter(pk=channelID)

        # if needed elements are present, save new message
        if query_author.first() and query_channel.first():
            new_message = Message(
                content=data['content'],
                author=query_author.first(),
                channel=query_channel.first()
            )
            new_message.save()
        else:
            pass # TODO return error 422

    response = []
    if channelID:
        response = Message.objects.filter(channel__id__contains=channelID)

    # preparing http response
    parsed_response = []

    # serializing response
    for message in response:
#   id: string;
#   channelId: string;
#   userId: string;
#   content: string;
#   createdAt: string;
        parsed_response.append({
            "id": str(message.pk),
            "channelId": str(message.channel),
            "userId": str(message.author.id),
            "content": message.content,
            "createdAt": message.created_at.isoformat()
        })

    return JsonResponse(parsed_response, safe=False, json_dumps_params={'ensure_ascii': False})
