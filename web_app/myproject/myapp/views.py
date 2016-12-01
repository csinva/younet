# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
import random
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.exceptions import *
from django.conf import settings
from keras.models import load_model
import numpy as np
import pickle


def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


char_indices = pickle.load(open(settings.PROJECT_ROOT + '/myapp/char_indices.p', 'rb'))
indices_char = pickle.load(open(settings.PROJECT_ROOT + '/myapp/indices_char.p', 'rb'))

model = load_model(settings.PROJECT_ROOT + '/myapp/char_rnn.h5')

response_length = 50
prev = ''


def search(request):
    search_title = request.POST.get('textfield', None)
    print('searching....', search_title)
    prev = (prev + search_title)[-40:]
    if len(prev) < 40:
        prev = ' ' * (40 - len(prev)) + prev
    message = ''
    for i in range(response_length):
        x = np.zeros((1, len(prev), len(char_indices)))
        for t, char in enumerate(prev):
            x[0, t, char_indices[char]] = 1.
        preds = model.predict(x, verbose=0)[0]
        next_char = indices_char[sample(preds, temperature=0.5)]
        response += next_char
        prev = prev[1:] + next_char
    return render_to_response(
        'myapp/list.html',
        {'message': message},
        context_instance=RequestContext(request)
    )


def list(request):
    return render_to_response(
        'myapp/list.html',
        {'message': ""},
        context_instance=RequestContext(request)
    )
