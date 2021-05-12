from rest_framework.pagination import PageNumberPagination


class ThreeNumberPagination(PageNumberPagination):
    """Define that a page can load 3 element max"""

    page_size = 3
