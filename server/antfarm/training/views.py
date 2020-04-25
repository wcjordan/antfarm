import json
import requests

from django.core import serializers
from django.http import HttpResponseBadRequest, JsonResponse

from antfarm.training.models import TrainingEpisodeModel, TrainingStepModel, TrainingRunModel


def episodes(request):
    validation = _ensure_valid_request_type(request, ['POST'])
    if validation is not None:
        return validation

    body = json.loads(request.body.decode('utf-8'))
    training_run = TrainingRunModel.objects.get(id=body['training_run_id'])
    new_object = TrainingEpisodeModel.objects.create(
        iteration=body['iteration'], total_reward=0, training_run=training_run)

    return JsonResponse({
        'id': new_object.id,
        'iteration': new_object.iteration,
        'total_reward': new_object.total_reward,
        'training_run_id': new_object.training_run.id,
    })


def episode(request, id):
    validation = _ensure_valid_request_type(request, ['PUT'])
    if validation is not None:
        return validation

    body = json.loads(request.body.decode('utf-8'))

    existing_object = TrainingEpisodeModel.objects.get(id=id)
    existing_object.total_reward=body['total_reward']
    existing_object.save()

    return JsonResponse({
        'id': existing_object.id,
        'iteration': existing_object.iteration,
        'total_reward': existing_object.total_reward,
        'training_run_id': existing_object.training_run.id,
    })


def steps(request):
    validation = _ensure_valid_request_type(request, ['POST'])
    if validation is not None:
        return validation

    body = json.loads(request.body.decode('utf-8'))
    episode = TrainingEpisodeModel.objects.get(id=body['episode_id'])
    new_object = TrainingStepModel.objects.create(iteration=body['iteration'],
                                                  action=body['action'],
                                                  state=body['state'],
                                                  reward=body['reward'],
                                                  is_done=body['is_done'],
                                                  info=body['info'],
                                                  episode=episode)

    return JsonResponse({
        'id': new_object.id,
        'iteration': new_object.iteration,
        'action': new_object.action,
        'state': new_object.state,
        'reward': new_object.reward,
        'is_done': new_object.is_done,
        'info': new_object.info,
        'episode_id': new_object.episode.id,
    })


def training_runs(request):
    validation = _ensure_valid_request_type(request, ['POST', 'PUT'])
    if validation is not None:
        return validation

    body = json.loads(request.body.decode('utf-8'))

    crud_op = request.META.get('HTTP_X_HTTP_METHOD_OVERRIDE')
    print(crud_op)
    if crud_op == 'POST':
        instance = TrainingRunModel.objects.create(name=body['name'])
        _make_learning_service_request(instance.id)
    else:
        instance = TrainingRunModel.objects.get(id=body['id'])
        instance.name = body.get('name', instance.name)
        instance.status = body.get('status', instance.status)
        instance.save()

    return JsonResponse({
        'id': instance.id,
        'name': instance.name,
        'status': instance.status,
    })


def _make_learning_service_request(id):
    data = {
        'id': id,
    }
    headers = {
        'content-type': 'application/json',
    }
    req = requests.post(
        'http://learning:8000/start_training_run',
        headers=headers,
        json=data)

    assert req.status_code == 204, 'Expected status 204, received {}.'.format(req.status_code)


def _ensure_valid_request_type(request, request_types):
    if request.method != 'POST':
        return HttpResponseBadRequest(
            "This endpoint only accepts POST requests.  "
            "Use the X-HTTP-Method-Override header to specify the desired "
            "CRUD operation.")

    crud_op = request.META.get('HTTP_X_HTTP_METHOD_OVERRIDE')
    if crud_op is None:
        return HttpResponseBadRequest(
            "Please set the X-HTTP-Method-Override header to specify the "
            "desired CRUD operation.")

    if not crud_op in request_types:
        return HttpResponseBadRequest(
            "The X-HTTP-Method-Override header must be "
            "one of the following: {}".format(request_types))

    return None
