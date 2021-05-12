from rest_framework import generics
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from ebooks_api.api.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly
from ebooks_api.models import Ebook, Review
from ebooks_api.api.serializers import EbookSerializer, ReviewSerializer


class EbookListCreateAPiView(generics.ListCreateAPIView):
    """Manages Ebook view endpoints"""

    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly, ]


class EbookDetailAPiView(generics.RetrieveUpdateDestroyAPIView):
    """Manages single Ebook Retrieve update destroy Endpoints"""

    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


class ReviewCreateAPiVeiw(generics.CreateAPIView):
    """Manages Review create api endpoints"""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Save Review to the Specific eBook"""
        review_author = self.request.user

        ebook_pk = self.kwargs.get('ebook_pk')
        ebook = generics.get_object_or_404(Ebook, pk=ebook_pk)

        curr_user_review = Review.objects.filter(
            ebook=ebook, review_author=review_author)

        if curr_user_review.exists():
            """As user already reviewed theis"""
            raise ValidationError('You already have reviewed this book!')
        serializer.save(ebook=ebook, review_author=review_author)


class ReviewDetailAPiView(generics.RetrieveUpdateDestroyAPIView):
    """Manages Endpoint to Retrieve Update and Destroy Review"""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly, ]

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
