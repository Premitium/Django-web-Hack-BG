import json
from django.http import JsonResponse, HttpResponse
from storage.services import create_user, store_data, get_value_with_key, delete_key_value, create_histogram
from storage.exceptions import UserDoestNotExistException
from uuid import UUID

#http://127.0.0.1:8000/api/storage/create-user/
def create_user_view(request):
    identifier = create_user()
    return JsonResponse({'identifier': identifier})

def store_data_view(request, identifier):
    if request.method != 'POST':
        return HttpResponse(status=405)
    data = json.loads(request.body.decode('utf-8'))

    try:
        store_data(identifier=identifier, data=data)
    except UserDoestNotExistException:
        return JsonResponse({'error':'User does not exist'}, status=404)
    else:
        return JsonResponse(data, status=201)

def manage_key_view(request, identifier, key):
    if request.method == 'GET':
        return get_key_view(request, identifier, key)
    if request.method == 'DELETE':
        return delete_key_view(request, identifier, key)
    else:
        return JsonResponse(status=405)

def delete_key_view(request, identifier, key):
    try:
        value = delete_key_value(identifier=identifier, key=key)
    except UserDoestNotExistException:
        return JsonResponse({'error':'User does not exist'}, status=404)
    if value is None:
        return JsonResponse({'error':'No such key'},status=404)
    return HttpResponse(status=202)

def get_key_view(request, identifier, key):
    try:
        value = get_value_with_key(identifier=identifier, key=key)
    except UserDoestNotExistException:
        return JsonResponse({'error': 'User does not exists'}, status=404)

    if value is None:
        return JsonResponse({'error': 'Key not found'}, status=404)
    return JsonResponse({'value': value})
