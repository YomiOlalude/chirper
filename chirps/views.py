from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views import generic
from .serializers import *
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated



# Create your views here.


@api_view(["GET"])
def chirps_list_view(request, *args, **kwargs):
    queryset = Chirp.objects.all()
    serializer = ChirpSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@authentication_classes(SessionAuthentication)
@permission_classes([IsAuthenticated])
def chirp_create_view(request, *args, **kwargs):
    serializer = ChirpSerializer(data=request.POST or None)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def chirp_detail_view(request, chirp_id, *args, **kwargs):
    queryset = Chirp.objects.filter(id=chirp_id)
    if not queryset.exists():
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    obj = queryset.first()
    serializer = ChirpSerializer(obj)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST", "DELETE"]) 
@permission_classes([IsAuthenticated])   
def chirp_delete_view(request, chirp_id, *args, **kwargs):
    queryset = Chirp.objects.filter(id=chirp_id)
    if not queryset.exists():
        return Response({}, status=status.HTTP_404_NOT_FOUND)
    queryset = queryset.filter(user=request.user)
    if not queryset.exists():
        return Response({"message": "You cannot delete this chirp"}, status=status.HTTP_401_UNAUTHORIZED)
    obj = queryset.first()
    obj.delete()
    return Response({"message": "Chirp deleted"}, status=status.HTTP_200_OK)

    
@api_view(["POST"]) 
@permission_classes([IsAuthenticated])   
def chirp_action_view(request, chirp_id, *args, **kwargs):
    
    '''
    Action options: like, unlike, rechirp
    '''

    serializer = ChirpActionSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        chirp_id = data.get("id")
        action = data.get("action")
        content = data.get("content")
            
        queryset = Chirp.objects.filter(id=chirp_id)
        if not queryset.exists():
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        obj = queryset.first()
        if action == "like":
            obj.likes.add(request.user)
        elif action == "unlike":
            obj.likes.remove(request.user)
        elif action == "rechirp":
            new_chirp = Chirp.objects.create(user=request.user, parent=obj, content=content)
            serializer = ChirpSerializer(new_chirp)
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"message": "Tweet removed"}, status=status.HTTP_200_OK)



# def chirps_list_view(request, *args, **kwargs):
#     chirps = Chirp.objects.all()
#     print(request.user)
#     context = {
#         "chirps": chirps
#     }

#     return render(request, "pages/home.html", context)


# def chirp_create_view(request, *args, **kwargs):
#     form = ChirpCreateForm(request.POST)
#     content = request.POST.get("content")
    
#     if form.is_valid():
#         form.save()
#         form = ChirpCreateForm()
#         return redirect("/")
        
#     context = {
#         "form": form
#     }
        
#     return render(request, "components/form.html", context)
    
