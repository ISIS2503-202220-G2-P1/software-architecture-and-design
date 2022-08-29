from .logic import variables_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def variables_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            variable_dto = vl.get_variable(id)
            variable = serializers.serialize('json', [variable_dto,])
            return HttpResponse(variable, 'application/json')
        else:
            variables_dto = vl.get_variables()
            variables = serializers.serialize('json', variables_dto)
            return HttpResponse(variables, 'application/json')

    if request.method == 'POST':
        variable_dto = vl.create_variable(json.loads(request.body))
        variable = serializers.serialize('json', [variable_dto,])
        return HttpResponse(variable, 'application/json')

@csrf_exempt
def variable_view(request, pk):
    if request.method == 'GET':
        variable_dto = vl.get_variable(pk)
        variable = serializers.serialize('json', [variable_dto,])
        return HttpResponse(variable, 'application/json')

    if request.method == 'PUT':
        variable_dto = vl.update_variable(pk, json.loads(request.body))
        variable = serializers.serialize('json', [variable_dto,])
        return HttpResponse(variable, 'application/json')
