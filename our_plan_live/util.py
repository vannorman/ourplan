#TODO https://github.com/sdispater/pendulum -- python datetimes made easy

import sys
import json
import threading
import datetime
import uuid
import traceback
import time
import random
import urllib

from django.db.models.base import ObjectDoesNotExist
from itertools import chain
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.middleware import csrf
from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.utils.encoding import smart_str
import sqlite3

def create_or_open_db(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      first_name TEXT,
                      last_name TEXT);''')
        conn.commit()
    except Error as e:
        print(e)

    return conn

# from our_plan_live.models import *
# from our_plan_live.forms import *

def alphaencode(number, alphabet='123456789ABCDEFGHJKLMNPRTUVWXYZabcdefghjkmnopqrstuvwxyz'):
    code = ''
    if 0 <= number < len(alphabet):
        return alphabet[number]
    while number != 0:
        number, i = divmod(number, len(alphabet))
        code = alphabet[i] + code
    return code

def client_post(view):
    return csrf_exempt(require_http_methods(['POST'])(view))

def client_get(view):
    return csrf_exempt(require_http_methods(['GET'])(view))

def get_or_create_csrf_token(request):
    token = request.META.get('CSRF_COOKIE', None)
    if token is None:
        token = csrf._get_new_csrf_string()
        request.META['CSRF_COOKIE'] = token
    request.META['CSRF_COOKIE_USED'] = True
    return token

def json_response(obj):
    try:
        if obj['success'] == False:
            del obj['success']
    except KeyError:
        pass
    return JsonResponse(obj) 

def renderWithNav(request, template, obj = None, cookies = None):
    if obj is None:
        obj = {}    
    obj['safari'] = False
    obj["csrf"] = get_or_create_csrf_token(request)
    obj["version"] =  "?" + str(time.time())
    response = render(request, template, obj)
    return response




