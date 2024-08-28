from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
import json
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.shortcuts import get_object_or_404

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.create_user(
            username=data['username'],
            password=data['password'],
            email=data['email']
        )
        user.save()
        return JsonResponse({'message': 'Usuario registrado exitosamente'})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = authenticate(username=data['username'], password=data['password'])
        if user is not None:
            # Genera el token de acceso y de refresh
            refresh = RefreshToken.for_user(user)
            
            # Incluye los tokens en la respuesta junto con la información del usuario
            user_data = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'status' : 200,
            }
            return JsonResponse({'message': 'Inicio de sesión exitoso', 'user': user_data})
        else:
            return JsonResponse({'error': 'Credenciales incorrectas'}, status=400)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def get_user_info(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == 'GET':
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
        }
        return Response(user_data)

    if request.method == 'PUT':
        user.username = request.data.get('username', user.username)
        user.email = request.data.get('email', user.email)
        user.save()
        return Response({"message": "User updated successfully"}, status=status.HTTP_200_OK)