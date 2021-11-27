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


@api_view(['POST'])
def register_user(request):

    serializer = UserSerializer(data=request.data)
    #print('user serializer: ', serializer.data)
    if serializer.is_valid():
        user = serializer.save()
        print('User: ', user)
        serializer = UserSerializer(user, many=False)
        print('user serializer 2: ', serializer.data)
        serializer = ProfileSerializer(data=request.data)

        #print('profile serializer: ', serializer.data)
        if serializer.is_valid():
            profile = serializer.save()
            profile.user = user
            profile.save()
            print('Profile: ', user)
            serializer = ProfileSerializer(profile, many=False)
            #print('Profile serializer 2: ', serializer.data)
        else:
            print(serializer.errors)  # for debug
        return Response(serializer.data)



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
    serializer = TableSerializer(tables, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_table(request, pk):
    tables = Table.objects.get(id=pk)
    serializer = TableSerializer(tables, many=False)
    return Response(serializer.data)
