from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from ..users.permissions import IsAccountOwner

class GetDetailView:
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    def retrieve(self, request: Request, *args, **kwargs) -> Response:
        """
        Obtençao de usuário
        """
        id_value = kwargs[self.url_param_name]
        model_object = get_object_or_404(self.view_queryset, pk=id_value)

        self.check_object_permissions(request, model_object)

        serializer = self.view_serializer(model_object)

        return Response(serializer.data, status.HTTP_200_OK)

class PatchDetailView:
    def update(self, request: Request, *args, **kwargs) -> Response:
        """
        Atualização de usuário
        """
        id_value = kwargs[self.url_param_name]
        model_object = get_object_or_404(self.view_queryset, pk=id_value)

        self.check_object_permissions(request, model_object)

        serializer = self.view_serializer(model_object, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)

class DeleteDetailView:
    def destroy(self, request: Request, *args, **kwargs) -> Response:
        """
        Deleçao de usuário
        """
        id_value = kwargs[self.url_param_name]
        model_object = get_object_or_404(self.view_queryset, pk=id_value)

        self.check_object_permissions(request, model_object)

        model_object.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class OnlyGetDetailView(GetDetailView, APIView):
    def get(self, request: Request, *args, **kwargs) -> Response:
        return super().retrieve(request, *args, **kwargs)

class OnlyPatchDetailView(PatchDetailView, APIView):
    def patch(self, request: Request, *args, **kwargs) -> Response:
        return super().update(request, *args, **kwargs)

class OnlyDeleteDetailView(GetDetailView, APIView):
    def delete(self, request: Request, *args, **kwargs) -> Response:
        return super().destroy(request, *args, **kwargs)

