from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from user.serializers import RegistrationSerializer
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'user/home.html')


@api_view(['POST',])

def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "successfully registered a new user."
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)