from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from ..models import Message
from django.core import serializers


@csrf_exempt  # ! FOR TEST PURPOSE ONLY - REMOVE IN PROD
def chat(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        print("CONTENT >>> {}".format(data['content']))
        new_message = Message(
            content=data['content'],
            date=data['date'],
            author=data['author'],
            channel=data['channel']
        )
        new_message.save()

    response = Message.objects.values()

    return JsonResponse(list(response), safe=False)
    # return HttpResponse(response)
