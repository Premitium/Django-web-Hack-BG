import os
import uuid
import json

from django.conf import settings

from .exceptions import UserDoestNotExistException
from .models import User, KeyValue
from collections import defaultdict

def uuid4():
    return str(uuid.uuid4())

#api.urls -> api.views -> storage.services - DB
def create_user():
    user = User.objects.create()

    return str(user.identifier)

def store_data(*, identifier, data):
    user = User.objects.filter(identifier=identifier).first()
    if not user:
        raise UserDoestNotExistException
    keyval = user.data.filter(key=data['key']).first()
    if keyval is None:
        keyval = KeyValue.objects.create(key=data['key'], value=data['value'], user=user)
        user.data.add(keyval)
    else:
        keyval.value = data['value']
        keyval.save()
    user.save()
    return data


def get_user_from_db(identifier):
    user = User.objects.filter(identifier=identifier).first()
    if user is None:
        raise UserDoestNotExistException
    return user


def create_histogram(objects):
    d = defaultdict(int)
    for o in objects:
        d[o] += 1

    return dict(d)

def get_value_with_key(*, identifier, key):
    user = get_user_from_db(identifier=identifier)
    if user is None:
        raise UserDoestNotExistException

    key_value = user.data.filter(key=key).first()
    if key_value is None:
        return None
    return key_value.value


def delete_key_value(*, identifier, key):
    user = get_user_from_db(identifier=identifier)
    if user is None:
        raise UserDoestNotExistException
    key_val = user.data.filter(key=key).first()

    if key_val is None:
        return None

    old_key = key_val.key
    user.data.filter(key=old_key).delete()
    user.save()
    return old_key
