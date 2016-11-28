# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
import random
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.exceptions import *


def search(request):
    search_title = request.POST.get('textfield', None)
    print('searching....', search_title)
    message = "THIS IS A RANDOM MESSAGE"
    return render_to_response(
        'myapp/list.html',
        {'message': message},
        context_instance=RequestContext(request)
    )


def list(request):
    return render_to_response(
        'myapp/list.html',
        {'message':""},
        context_instance=RequestContext(request)
    )
