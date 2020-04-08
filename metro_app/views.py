from rest_framework import generics
from rest_framework.response import Response

from .serializers import StationsSerializer

from .station import verify


class VerificateView(generics.GenericAPIView):
    serializer_class = StationsSerializer

    def post(self, request):
        res_dict = verify(request)

        return Response(res_dict)
