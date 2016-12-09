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

# char_indices = pickle.load(open(settings.PROJECT_ROOT + '/myapp/char_indices_3.p', 'rb'))
# indices_char = pickle.load(open(settings.PROJECT_ROOT + '/myapp/indices_char_3.p', 'rb'))
# model = load_model(settings.PROJECT_ROOT + '/myapp/char_rnn.h5')


def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


def search(request):
    response_length = 50
    prev = ''
    # search_title = request.POST.get('textfield', None)
    # print('searching....', search_title)
    # print("shape char_ind", len(char_indices))
    # print("shape indices_char", len(indices_char))
    # prev = (prev + search_title)[-40:]
    # if len(prev) < 40:
    #     prev = ' ' * (40 - len(prev)) + prev
    response = 'SAMPLE_RESPONSE'
    # for i in range(response_length):
    #     x = np.zeros((1, len(prev), len(char_indices)))
    # print("shape x", x.shape)
    # for t, char in enumerate(prev):
    # x[0, t, char_indices[char]] = 1.
    # preds = model.predict(x, verbose=0)[0]
    # next_char = indices_char[sample(preds, temperature=0.5)]
    # response += next_char
    # prev = prev[1:] + next_char
    return render_to_response(
        'myapp/list.html',
        {'message': response},
        context_instance=RequestContext(request)
    )


def list(request):
    return render_to_response(
        'myapp/list.html',
        {'message': ""},
        context_instance=RequestContext(request)
    )
