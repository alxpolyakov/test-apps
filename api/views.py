from rest_framework.views import APIView
from .permissions import ApiKeyPermission
from rest_framework.response import Response
from .models import App
from .serializers import AppSerializer


class AppsListView(APIView):
    permission_classes = [ApiKeyPermission]

    def get(self, request, format=None):
        qs = App.objects.all()
        serializer = AppSerializer(qs, many=True)
        return Response(serializer.data)
