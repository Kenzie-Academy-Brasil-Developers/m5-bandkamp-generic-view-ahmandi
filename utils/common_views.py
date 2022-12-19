from rest_framework.views import APIView, Request, Response, status
from rest_framework.pagination import PageNumberPagination

class PostCommonView(APIView):
    def post(self, request: Request) -> Response:

        serializer = self.view_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class GetCommonPaginatedView(APIView):
    def get(self, request, pk):

        model_object = self.objects.filter(album_id=pk)

        result_page = self.paginate_queryset(model_object, request)
        serializer = self.view_serializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)
