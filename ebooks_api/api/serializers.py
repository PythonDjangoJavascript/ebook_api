from rest_framework import serializers

from ebooks_api.models import Review, Ebook


class ReviewSerializer(serializers.ModelSerializer):
    """Serialize Review data"""

    class Meta:
        model = Review
        fields = '__all__'


class EbookSerializer(serializers.ModelSerializer):
    """Serializes Ebook Data"""

    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Ebook
        fields = '__all__'
