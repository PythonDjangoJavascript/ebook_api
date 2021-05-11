from rest_framework import generics
from rest_framework import mixins

from ebooks_api.models import Ebook
from ebooks_api.api.serializers import EbookSerializer


class EbookListCreateAPiView(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             generics.GenericAPIView):
    """Manages Ebookview endpoints"""

    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    def get(self, request, *args, **kwargs):
        """Handle get request and return Response"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Handle post request and create ebook object"""
        return self.create(request, *args, **kwargs)
