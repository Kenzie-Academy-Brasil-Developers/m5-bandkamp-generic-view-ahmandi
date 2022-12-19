from rest_framework.views import APIView, status, Response
from .models import Album
from .serializers import AlbumSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics


class AlbumView(generics.ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = AlbumSerializer


    queryset = Album.objects.all()

    # def get(self, request):
    #     """
    #     Obtençao de albums
    #     """
    #     albums = Album.objects.all()

    #     result_page = self.paginate_queryset(albums, request)
    #     serializer = AlbumSerializer(result_page, many=True)

    #     return self.get_paginated_response(serializer.data)
