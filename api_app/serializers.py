from rest_framework import serializers
from api_app.models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    store_name = serializers.CharField(max_length=50)
    description = serializers.CharField()
    image = serializers.ImageField(default='images', use_url=True)
    fave = serializers.BooleanField(default=False)


class BokModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
