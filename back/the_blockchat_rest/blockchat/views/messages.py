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

    # data = serializers.serialize('json', response)
    # return HttpResponse(data, content_type="application/json")

    parsed_response = []

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

    print("PARSED_RESPONCE > {}".format(parsed_response))

    return JsonResponse(parsed_response, safe=False, json_dumps_params={'ensure_ascii': False})

    # return JsonResponse(parsed_response, safe=False)
