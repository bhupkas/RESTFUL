from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from restful.models import Profile
from restful.serializers import ProfileSerializer

from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO


@api_view(['GET', 'POST'])
def profile_list(request):
    """
    List all tasks, or create a new task.
    """
    if request.method == 'GET':
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProfileSerializer(data = request.DATA)
        if serializer.is_valid():
			temp = Profile(name = serializer.validated_data.get('name') , phone = serializer.validated_data.get('phone'))
			temp.save()
			return Response(serializer.data)
			#serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def profile_detail(request, pk):
    """
    Get, udpate, or delete a specific task
    """
    try:
        profile = Profile.objects.get(pk=pk)
    except profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(task)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfileSerializer(task, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)