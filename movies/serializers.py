from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Movie, Rate, MovieOrder
from users.models import User
from users.serializers import AccountSerializer
import ipdb


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    duration = serializers.CharField(required=False)
    rating = serializers.ChoiceField(
        choices=Rate.choices,
        default=Rate.G,
        required=False,
    )
    synopsis = serializers.CharField(
        allow_null=True,
        default=None,
    )
    # user = AccountSerializer(
    #     write_only=True,
    # )
    added_by = serializers.SerializerMethodField()

    def create(self, validated_data: dict) -> Movie:
        # ipdb.set_trace()
        return Movie.objects.create(**validated_data)

    def get_added_by(self, obj):
        return obj.user.email


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    price = serializers.DecimalField(
        max_digits=8,
        decimal_places=2,
    )
    buyed_by = serializers.SerializerMethodField()
    buyed_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data: dict) -> MovieOrder:
        return MovieOrder.objects.create(**validated_data)

    def get_title(self, obj: MovieOrder) -> str:
        return obj.movie.title

    def get_buyed_by(self, obj: MovieOrder) -> str:
        return obj.user.email
