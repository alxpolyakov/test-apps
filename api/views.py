from rest_framework.views import APIView
from .permissions import ApiKeyPermission
from rest_framework.response import Response
from .models import App, ApiKey
from .serializers import AppSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AppsListView(APIView):
    permission_classes = [ApiKeyPermission]

    def get(self, request, format=None):
        qs = App.objects.all()
        serializer = AppSerializer(qs, many=True)
        return Response(serializer.data)


class CreateAPIKeyView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, format=None):
        ctx = {
            'key': ApiKey.objects.create(owner=request.user).key
        }
        return Response(ctx)
