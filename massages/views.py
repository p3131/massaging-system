from .models import Massage
from django.shortcuts import redirect
from rest_framework import viewsets
from .serializers import MassageSerializer
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse, HttpResponse
from rest_framework.request import Request
import json
from django.db.models import Q

# Create your views here.


class MassageViewSet(ModelViewSet):
    queryset = Massage.objects.all()
    serializer_class = MassageSerializer
    

@api_view(['GET'])
def all_massages(request):
    if not request.user.is_authenticated:
        return redirect(f"/massages/api-auth/login/?next={request.path}")
    if str(request.user)!='admin':
        queryset = Massage.objects.filter(Q(sender_first_name=str(request.user.first_name),sender_last_name=str(request.user.last_name)) | 
                                          Q(receiver_first_name=str(request.user.first_name),receiver_last_name=str(request.user.last_name)))
    else:
        queryset = Massage.objects.all()
    return JsonResponse({"results": list(queryset.values())})

@api_view(['GET'])
def massage_unread(request):
    if not request.user.is_authenticated:
        return redirect(f"/massages/api-auth/login/?next={request.path}")
    queryset = Massage.objects.filter(read_massage=False)
    if str(request.user)!='admin':
        queryset = queryset.filter(Q(sender_first_name=str(request.user.first_name),sender_last_name=str(request.user.last_name)) | 
                                   Q(receiver_first_name=str(request.user.first_name),receiver_last_name=str(request.user.last_name)))
    return JsonResponse({"results": list(queryset.values())})

@api_view(['GET'])
def read_massage(request):
    if not request.user.is_authenticated:
        return redirect(f"/massages/api-auth/login/?next={request.path}")
    queryset = Massage.objects.filter(read_massage=False)
    if str(request.user)!='admin':
        queryset = Massage.objects.filter(Q(sender_first_name=str(request.user.first_name),sender_last_name=str(request.user.last_name)) | 
                                          Q(receiver_first_name=str(request.user.first_name),receiver_last_name=str(request.user.last_name)))
    queryset = queryset[:1]
    return JsonResponse({"results": list(queryset.values())})

@api_view(['DELETE'])
def delete_massage(request, pk):
    if not request.user.is_authenticated:
        return redirect(f"/massages/api-auth/login/?next={request.path}")
    queryset = Massage.objects.all()
    if str(request.user)!='admin':
        queryset = queryset.filter(Q(sender_first_name=str(request.user.first_name),sender_last_name=str(request.user.last_name)) | 
                                   Q(receiver_first_name=str(request.user.first_name),receiver_last_name=str(request.user.last_name)))
    try:
        instance = queryset.get(pk=pk)
        instance.delete()
    except queryset.DoesNotExist:
        return JsonResponse({'error': 'massage not found.'}, status=404) 
    return JsonResponse({'message': 'massage deleted successfully.'})


@api_view(['POST'])
def create_massage(request):
    if not request.user.is_authenticated:
        return redirect(f"/massages/api-auth/login/?next={request.path}")   
    serializer = MassageSerializer(data=request.data, context={'request': request})
    if serializer.is_valid() and request.data['sender_first_name']==request.user.first_name and request.data['sender_last_name']==request.user.last_name:
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)