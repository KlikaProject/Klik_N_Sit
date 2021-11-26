from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from .serializers import *
from klikaapp.models import *
from users.models import *


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def get_routes(request):

    routes = [
      {'GET': '/api/'}
    ]

    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_details(request):
    user = User.objects.all()
    print(user.id)
    return_str = "User: " + str(user)

    return Response(return_str)


@api_view(['GET'])
def get_tables(request):
    tables = Table.objects.all()
    serializer = Table_serializer(tables, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_table(request, pk):
    tables = Table.objects.get(id=pk)
    serializer = Table_serializer(tables, many=False)
    return Response(serializer.data)
