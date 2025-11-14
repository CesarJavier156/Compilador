from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
import json

# Importamos nuestro método
from .utils import run_code

@api_view(['POST'])
def main(request):
    if request.method != 'POST':
        return JsonResponse(
            {'code': 'Método no permitido'},
            status=405
        )

    try:
        body = request.body.decode('utf-8') if request.body else ''
        data = json.loads(body) if body else {}
    except Exception:
        return JsonResponse(
            {'code': 'JSON inválido'},
            status=400
        )

    # Verificamos que el JSON tenga la clave 'text'
    code = data.get('text', '')
    output = run_code(code)

    return JsonResponse(
        {"output":output}
    )

