import json

from django.http import HttpResponseBadRequest, JsonResponse


def episodes(request):
    if request.method != 'POST':
        return HttpResponseBadRequest(
            "This endpoint only accepts POST requests.  "
            "Use the X-HTTP-Method-Override header to specify the desired CRUD operation."
        )

    crud_op = request.META.get('HTTP_X_HTTP_METHOD_OVERRIDE')
    if crud_op is None:
        return HttpResponseBadRequest(
            "Please set the X-HTTP-Method-Override header to specify the desired CRUD operation."
        )

    body = json.loads(request.body.decode('utf-8'))

    return JsonResponse({})