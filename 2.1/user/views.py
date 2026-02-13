from django.db.migrations import serializer
from rest_framework.response import Response

from .models import User
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UserSerializer


# Create your views here.

class UserListView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        data = {
            'status': status.HTTP_200_OK,
            'message': 'barcha userlar',
            'data': serializer.data
        }
        return Response(data)


class UserDetailView(APIView):
    def get(self, request, pk):
        user = User.objects.filtr(pk=pk).frist()
        serializer = UserSerializer(user , data=request.data)
        data = {
            'status': status.HTTP_200_OK,
            'massage':'user',
            'data': serializer.data
        }
        return Response(data)

class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_201_CREATED,
                'massage':'user yaratildi',
                'data': serializer.data
            }
            return Response(data)
        data = {
            'status': status.HTTP_400_BAD_REQUEST,
            'massage': 'Error',
            'desc': serializer.errors
        }
        return Response(data)


class UserDeleteView(APIView):
    def delete(self, request, pk):
        user = User.objects.filter(pk=pk).delete()
        if user is None:
            data = {
                'status': status.HTTP_404_NOT_FOUND,
                'massage': 'User topilmadi',
                'desc': serializer.errors
            }
            return Response(data)
        data = {
            'status': status.HTTP_204_NO_CONTENT,
            'massage': 'user ochirlidi',
            'data': user
        }
        return Response(data)


class UserUpdateView(APIView):
    def put(self, request, pk):
        product = User.objects.filter(pk=pk).first()
        serializer = UserSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'status': status.HTTP_200_OK,
            'message': 'user update',
            "data": serializer.data
        }

        return Response(data)

    def patch(self, request, pk):
        product = User.objects.filter(pk=pk).first()
        serializer = UserSerializer(product, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'status': status.HTTP_200_OK,
            'message': 'user update',
            "data": serializer.data
        }

        return Response(data)