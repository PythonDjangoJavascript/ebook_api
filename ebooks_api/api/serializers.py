from rest_framework import serializers

from ebooks_api.models import Review, Ebook


class ReviewSerializer(serializers.ModelSerializer):
    """Serialize Review data"""

    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('ebook',)


class EbookSerializer(serializers.ModelSerializer):
    """Serializes Ebook Data"""

    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Ebook
        fields = '__all__'
