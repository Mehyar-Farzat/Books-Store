from rest_framework import serializer
from .models import Auther, Book, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class AutherListSerializer(serializer.ModelSerializer):
    book = serializers.StringRelatedField()
    class Meta:
        model = Auther
        fields = '__all__'

class AutherDetailSerializer(serializer.ModelSerializer):
    book = serializers.StringRelatedField()
    class Meta:
        model = Auther
        fields = '__all__'

    


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookDetailSerializer(serializers.ModelSerializer):
    Auther = serializers.StringRelatedField()
    reviews = ReviewSerializer(many=True, source ='book_review')
    reviews_count = serializers.SerializerMethodField()
    avg_rate = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_reviews_count(self,object):
        reviews_count= object.review_book.all().count()
        return reviews_count

    def get_avg_rate(self,object):
        total = 0
        reviews = object.review_book.all()
        for review in reviews:
            total += review.rate
        if reviews :
            return total/len(reviews)
        else:
            return 0
