from rest_framework.views import APIView, Request, Response, status
from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404
from .permissions import IsAccountOwner
from utils.common_views import PostCommonView
from utils.detail_common_view import OnlyGetDetailView, OnlyPatchDetailView, DeleteDetailView


class UserView(PostCommonView):
    view_serializer = UserSerializer
class UserDetailView(OnlyGetDetailView, OnlyPatchDetailView, DeleteDetailView):
    view_serializer = UserSerializer
    view_queryset = User.objects.all()

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]