from rest_framework import generics
from rest_framework import mixins

from ebooks_api.models import Ebook
from ebooks_api.api.serializers import EbookSerializer


class EbookListCreateAPiView(generics.ListCreateAPIView):
    """Manages Ebook view endpoints"""

    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


class EbookDetailAPiView(generics.RetrieveUpdateDestroyAPIView):
    """Manages single Ebook Retrieve update destroy Endpoints"""

    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    # Just for Practice how concrete classes work under the hood
    # class EbookListCreateAPiView(mixins.ListModelMixin,
    #                              mixins.CreateModelMixin,
    #                              generics.GenericAPIView):
    #     """Manages Ebookview endpoints"""

    #     queryset = Ebook.objects.all()
    #     serializer_class = EbookSerializer

    #     def get(self, request, *args, **kwargs):
    #         """Handle get request and return Response"""
    #         return self.list(request, *args, **kwargs)

    #     def post(self, request, *args, **kwargs):
    #         """Handle post request and create ebook object"""
    #         return self.create(request, *args, **kwargs)
