from django.shortcuts import render
from django.http import HttpResponse, JsonResponse 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Verbos
from .serializers import VerbosSerializer

@csrf_exempt
def verbos_list(request):
    """
    List all Verbos instances

    """

    if request.method == 'GET':
        verbos = Verbos.objects.all()
        serializer = VerbosSerializer(verbos, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VerbosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def verbos_detail(request,pk):
    """
    Retrieve, update or delete a verbos instance
    """

    try:
        verbo = Verbos.objects.get(pk=pk)
    except Verbos.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VerbosSerializer(verbo)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VerbosSerializer(verbo,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == "DELETE":
        verbo.delete()
        return HttpResponse(status=204)

